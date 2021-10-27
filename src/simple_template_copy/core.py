from pathlib import Path
import os
from typing import Dict, List
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import shutil
import logging


def order_match(str1, str2):
    """order_match"""
    l1 = len(str1)
    l2 = len(str2)
    i = 0
    j = 0

    if l1 > l2:
        return 0

    while i < l1 and j < l2:
        if str1[i] == str2[j]:
            i += 1
            j += 1
        else:
            j += 1
    return 100 * (i / l1)


class CopyTemplate:
    def __init__(
        self,
        template_str: str,
        target_strs: List[str],
        no_exec=False,
        help_message="",
        log_level=logging.INFO,
    ):
        """CopyTemplate"""
        # print("here")

        # variable define
        self.log_level = log_level
        self.template_str = template_str
        self.target_strs = target_strs
        self.template_path = None
        self.target_paths = None
        self.help_message = help_message

        self.feedback_messages = []

        self.has_template_str = True
        self.has_target_str = True
        self.possible_templates = []
        self.find_template_num = 0
        self.is_path_ts = False  # template str is exist path
        # this may not be good

        self.target_str_exists = False

        # tag: template_dir
        self.template_dir = "~/tempy_templates_dir"  # default path

        self.template_names = []
        self.template_name_path_map = dict()
        self.simple_matched = False
        self.possible_matched = False

        self.pre_treatment()

        self.info()
        self.main()
        self.lastline_summary()

        # if help:
        #     self.help()

    def log_config(self):
        """log_config"""
        self.ch = logging.StreamHandler()
        self.ch.setLevel(self.log_level)

        self.formatter = logging.Formatter(
            "|%(asctime)s|%(name)s|%(levelname)s|\n%(message)s\n"
        )

        self.ch.setFormatter(self.formatter)

        self.logger = logging.Logger("CopyTemplate")
        self.logger.setLevel(logging.DEBUG)

        self.logger.addHandler(self.ch)

    def load_config(self):
        """load_config"""
        # tag: load env config
        osvar = os.getenv("tempy_templates_dir")

        if osvar:
            self.template_dir = osvar

    def pre_treatment(self):
        """pre_treatment"""
        self.log_config()
        self.load_config()

        self.template_dir_path = self.path_solve(self.template_dir)
        if not self.template_dir_path.exists():
            self.template_dir_path.mkdir()

        if self.template_str is None:
            self.template_str = ""
            self.has_template_str = False

        # check variable type?
        if self.target_strs is None or self.target_strs == []:
            self.target_str = []
            self.has_target_str = False

        self.template_str.strip()
        self.target_strs = list(map(str.strip, self.target_strs))

        if self.has_template_str and self.path_solve(self.template_str).exists():
            self.is_path_ts = True
            self.template_path = self.path_solve(self.template_str)

        # self.template_path = self.path_solve(self.template_str)

        # template_str_process
        if self.has_template_str and not self.is_path_ts:
            # prepare possible tempalte path
            self.data_prepare()

            self.find_possible_template()

            self.simple_match()

        # target str process
        if self.has_target_str:
            self.target_paths = list(map(self.path_solve, self.target_strs))

    def info(self):
        """info"""
        self.logger.debug("hello")

    def main(self):
        """main"""
        if self.has_template_str:
            self.print_possible_templates()
            self.print_simple_match()

            #
            if self.has_target_str and (
                self.simple_matched or self.possible_matched or self.is_path_ts
            ):

                self.copy_template()

                self.print_copy_info()
            # else:
            #     # only show possible template path
            #     self.print_possible_templates()
        else:
            print(self.help_message)

        return
        # self.feedback_messages.append("help message")

    def help(self):
        """help"""
        pass

    def path_solve(self, path_str):
        """path_solve"""
        return Path(path_str).expanduser().resolve()

    def simple_match(self):
        """simple_match"""
        if self.template_str in self.template_names:
            self.simple_matched = True
            self.template_path = self.template_name_path_map[self.template_str]

    def data_prepare(self):
        """data_prepare"""
        for path in self.template_dir_path.iterdir():  # tag: bug?
            self.template_names.append(path.name)
            self.template_name_path_map[path.name] = path

    def find_possible_template(self):
        """find_possible_template"""
        # data prepare

        names_scores = process.extract(
            self.template_str, self.template_names, scorer=order_match
        )
        matchs = list(filter(lambda x: x[1] >= 90, names_scores))

        self.find_template_num = len(matchs)
        for match in matchs:
            self.possible_templates.append(
                (match[0], self.template_name_path_map[match[0]])
            )

        if self.find_template_num == 1:
            self.template_path = self.possible_templates[0][1]
            self.possible_matched = True

    def print_possible_templates(self):
        """print_possible_templates"""
        print(f"find {len(self.possible_templates)} possible templates below")
        for template in self.possible_templates:
            print(template[0], " : ")
            print("    ", template[1])
        print()

    def print_simple_match(self):
        """print_possible_templates"""
        if self.simple_matched:
            print("simple matched")
            print(self.template_str, " : ")
            print("    ", self.template_path)
        else:
            print("no simple matched")

        print()

    def copy_template(self):
        """copy_template"""
        if self.template_path.is_dir():
            for target_path in self.target_paths:
                shutil.copytree(
                    str(self.template_path), str(target_path), dirs_exist_ok=True
                )
        elif self.template_path.is_file():
            for target_path in self.target_paths:
                shutil.copy(str(self.template_path), str(target_path))

    def print_copy_info(self):
        """print_copy_info"""
        print("copy " + str(self.template_path))
        print("to")
        print(" , ".join(self.target_strs))
        print()

    def lastline_summary(self):
        """lastline_summary"""
        lastline = ""
        if self.has_template_str:
            lastline += "get template str, "
            if self.simple_matched:
                lastline += "simple matched, "

            if self.has_target_str and (
                self.simple_matched or self.possible_matched or self.is_path_ts
            ):
                lastline += "file copyed, "
        else:
            lastline += "no input get,show help message on top"
        print(lastline)

    def custom_copy(self, argvs):
        """custom_copy"""
        pass


# if __name__ == "__main__":
#     t = CopyTemplate()