# -*- coding: utf-8 -*-

# @author bl4ckvghost
#
# Copyright (C) 2017 Youssef Hesham
#
# License <http://www.gnu.org/licenses/gpl-3.0.html>

"""
***WHAT IS THIS ALL ABOUT?***
This is the main runnable file.
"""

import sys
from core import Check, Control

# Creating instances
check_req = Check.Check_req()
looprocess = Control.LoopControl()

# Initializing Variables
action = ''
# Commands for the user to input
commands = ['--gui', '--cli', '--help', '--about',
            '--easy_mode', '--about_me', '--license',
            '--vault', '--license', '--attacks',
            '--version', '--extract']

try:
    action = sys.argv[1]
except Exception as e:
    pass


def main():
    """Main Function."""
    check_req.check_py_version()  # Check valid python version
    check_req.check_os()  # Checking the required operation system
    check_req.check_user()  # Check if the user is root or not
    if action == '':
        from core.Banner import Printer
        printer = Printer()
        printer.main_banner()
#   check_req.check_softwares()
    looprocess.main_loop(action=action, commands=commands)  # Run


if __name__ == '__main__':
    main()
