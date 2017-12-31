# -*- coding: utf-8 -*-

# @author bl4ckvghost
#
# Copyright (C) 2017 Youssef Hesham
#
# License <http://www.gnu.org/licenses/gpl-3.0.html>

import sys
from core import Check, Control

# Creating instances
check_req = Check.Check_req()
run = Control.LoopControl()

# Initializing Variables
action = ''
# Commands for the user to input
commands = ['--gui'      , '--cli'     , '--help',
            '--easy_mode', '--about_me', '--license',
            '--vault'    , '--set'     , '--attacks',
            '--version'  , '--extract' , '--about',
            '--install']

try:
    action = sys.argv[1]
except Exception as e:
    pass


def main():
    """Main Function."""
    check_req.check_py_version()
    check_req.check_os()
    check_req.check_user()
#   check_req.check_softwares()
    if action == '':
        from core.Banner import Printer
        printer = Printer()
        printer.main_banner()
    run.main_loop(action=action, commands=commands)  # Run


if __name__ == '__main__':
    main()
