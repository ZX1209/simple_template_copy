import os
from pathlib import Path
from docopt import docopt
import logging as log
import shutil
import sys
from . import core  # relative import just in package

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


def main():
    """main"""
    arguments = docopt(doc, version="Copy Template 0.4")

    # set log level
    log_map = {"debug": log.DEBUG, "info": log.INFO, "warn": log.WARN}
    log_level = log_map.get(arguments.get("--log_level").lower())
    log.basicConfig(level=log_level)
    # check arguments
    log.debug(arguments)

    core.CopyTemplate(
        arguments.get("<template_str>"),
        arguments.get("<target_str>"),
        log_level=log_level,
    )
