# -*- coding: utf-8 -*-

# @author bl4ckvghost
#
# Copyright (C) 2017 Youssef Hesham
#
# License <http://www.gnu.org/licenses/gpl-3.0.html>

import os
import sys
import platform
from core import Banner, gui, Obevilion

arg = ['--gui', '--cli', '--help']

printer = Banner.Printer()
try:
    action = sys.argv[1]
except Exception as e:
    printer.main_banner()

def runCLI(arg1, arg2):
    Obevilion.script(path=arg1, limit=arg2)

def main():
    try:
        assert action in arg, "Action is not one of [ --gui, --cli, --help, -g, -c, -h]"
        if action is '--gui':
            gui.main()
        elif action is '--cli':
            runCLI(sys.argv[2], limit=3)
        elif action is '--help':
            printer.help_banner()
        else:
            printer.main_banner() # Just For Now
    except Exception as e:
        try:
            if sys.argv[1] is not arg:
                printer.invalid_input()
            else:
                pass
        except Exception as e:
            pass

if __name__ == '__main__':
    main()
