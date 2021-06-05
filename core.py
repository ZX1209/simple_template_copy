from pathlib import Path
import os
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


class CopyTemplate:
    def __init__(
        self, template_str: str = "", target_str: str = "", no_exec=False, help=False
    ):
        """CopyTemplate"""
        # variable define
        self.template_str = template_str.strip()  # 类型检查什么的确实有存在的必要啊
        self.target_str = target_str.strip()
        self.find_template_num = 0
        self.target_str_exists = False
        self.has_template_str = False
        self.has_target_str = False
        self.is_path_ts = False  # template str is exist path
        self.template_dir = "./test/templates/"  # just for test

        self.state_detect()

        # exec?
        if no_exec:
            pass
        else:
            self.main()

        if help:
            self.help()

        self.info()

    def state_detect(self):
        """state_detect"""
        if self.template_str != "":
            self.has_template_str = True

        if self.target_str != "":
            self.has_template_str = True

        if self.has_template_str and self.path_solve(self.template_str).exists():
            self.is_path_ts = True

    def info(self):
        """info"""
        print(self.__dict__)

    def main(self):
        """main"""
        pass

    def help(self):
        """help"""
        pass

    def path_solve(self, path_str):
        """path_solve"""
        return Path(path_str).expanduser().resolve()

    def find_possible_template(self):
        """find_possible_template"""
        pass

    def describe_match(self, pattern_str, given_str):
        """describe_match
        use fuzzywuzzy now
        """
        pass

    def solve_target_path(self, target_path):
        """solve_target_path"""
        pass

    def copy_template(self, template_path, target_path):
        """copy_template"""
        pass


if __name__ == "__main__":
    t = CopyTemplate()