# -*- coding: utf-8 -*-

# @author bl4ckvghost
#
# Copyright (C) 2017 Youssef Hesham
#
# License <http://www.gnu.org/licenses/gpl-3.0.html>

import sys
from core import Banner, gui, Obevilion, Check, Control

check_req  = Check.Check_req()
printer    = Banner.Printer()
looprocess = Control.LoopControl()

try:
    action = sys.argv[1]
except Exception as e:
    printer.main_banner()

def runCLI(arg1, arg2):
    # Obevilion.script(path=arg1, limit=arg2)
    pass

def main():

    check_req.check_os() # Checking the required operation system
    check_req.check_py_version() # Check valid python version

    try:
        assert action in ['--gui', '--cli', '--help', '--about', 'easy_mode'], "Action is not one of [ --gui, --cli, --help, --about, --easy_mode ]"
        if action == '--gui':
            gui.main()
        elif action == '--cli':
            # runCLI(sys.argv[2], limit=3)
            print("Not Working Right Now")
        elif action == '--help':
            printer.help_banner()
        elif action == '--about':
            printer.about()
    except Exception as e:
        try:
            if sys.argv[1] is not '--gui' or '--cli' or '--help':
                printer.invalid_input()
            else:
                pass
        except Exception as e:
            pass

if __name__ == '__main__':
    main()
