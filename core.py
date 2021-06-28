from pathlib import Path
import os
from typing import Dict
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
        target_str: str,
        no_exec=False,
        help=False,
        log_level=logging.INFO,
    ):
        """CopyTemplate"""

        # variable define
        self.log_level = log_level
        self.template_str = template_str
        self.target_str = target_str
        self.template_path = None
        self.target_path = None

        self.feedback_messages = []

        self.has_template_str = True
        self.has_target_str = True
        self.possible_templates = []
        self.find_template_num = 0
        self.is_path_ts = False  # template str is exist path
        # this may not be good

        self.target_str_exists = False

        self.template_dir = "./test/templates/"  # just for test

        self.template_names = []
        self.template_name_path_map = dict()
        self.simple_matched = False
        self.possible_matched = False

        self.pre_treatment()

        self.info()
        self.main()

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

        if self.template_str is None:
            self.template_str = ""
            self.has_template_str = False

        if self.target_str is None:
            self.target_str = ""
            self.has_target_str = False

        self.template_str.strip()
        self.target_str.strip()

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
            self.target_path = self.path_solve(self.target_str)

    def info(self):
        """info"""
        self.logger.debug("hello")

    def main(self):
        """main"""
        if self.has_template_str:

            #
            if self.has_target_str and (
                self.simple_matched or self.possible_matched or self.is_path_ts
            ):

                self.copy_template()
            else:
                # only show possible template path
                self.print_possible_templates()
        else:
            print("show help messages")

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
        for path in self.template_dir_path.iterdir():
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
        print("too much possible templates below")
        for template in self.possible_templates:
            print(template[0], " : ")
            print("    ", template[1])

    def copy_template(self):
        """copy_template"""
        if self.template_path.is_dir():
            shutil.copytree(str(self.template_path), str(self.target_path))
        elif self.template_path.is_file():
            shutil.copy(str(self.template_path), str(self.target_path))


# if __name__ == "__main__":
#     t = CopyTemplate()