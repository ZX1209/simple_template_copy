class CopyTemplate(Object):
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

        self.state_detect()

        # exec?
        if no_exec:
            pass
        else:
            self.main()

        if help:
            self.help()

    def state_detect(self):
        """state_detect"""
        if self.template_str != "":
            self.has_template_str = True

        if self.target_str != "":
            self.has_template_str = True

    def main(self):
        """main"""
        pass

    def help(self):
        """help"""
        pass

    def describe_match(self, pattern_str, given_str):
        """describe_match"""
        pass

    def solve_target_path(self, target_path):
        """solve_target_path"""
        pass

    def copy_template(self, template_path, target_path):
        """copy_template"""
        pass
