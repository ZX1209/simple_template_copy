import os
from pathlib import Path
from docopt import docopt
import logging as log
import shutil
import sys
from core import CopyTemplate

doc = """simple template copy by python

Usage:
    cmd.py [options]
    cmd.py <template_str>  [options]
    cmd.py <template_str> <target_str> [options]

Options:
    -h ,--help     Show this screen.
    -v,--version     Show version.
    --log_level=<level>  logging.log level[default: info]
    template_str    template describe str
    target_str     target name clare


Docs:
    cmd.py : show useful optioon? and all templates name
    cmd.py <template_str> : search template by template_str
    cmd.py <template_str> <target_str> : complate copy

"""
test_cmd = """



"""


def copy_from_template(src, dst):
    """copy_from_template 模板复制

    Args:
        src (Path Like): 源文件或源文件路径
        dst (Path Like): 目标位置包含目标文件名或目录名,非符号连接
    Todo:
        handle errors

    """
    # dst, path,name
    if Path.is_dir(src):
        shutil.copy(src, dst)  # dst be the target path(not created)
    elif Path.is_file(src):
        shutil.copy(src, dst)


if __name__ == "__main__":
    arguments = docopt(doc, version="Copy Template 0.3")

    # set log level
    log_map = {"debug": log.DEBUG, "info": log.INFO, "warn": log.WARN}
    log_level = log_map.get(arguments.get("--log_level").lower())
    log.basicConfig(level=log_level)
    # check arguments
    log.debug(arguments)

    CopyTemplate(
        arguments.get("<template_str>"),
        arguments.get("<target_str>"),
        log_level=log_level,
    )
