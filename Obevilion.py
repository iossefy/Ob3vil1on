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

printer = Banner.Printer()
try:
    action = sys.argv[1]
except Exception as e:
    printer.main_banner()

def runCLI(arg1, arg2):
    Obevilion.script(path=arg1, limit=arg2)

def main():
    try:
        assert action in ['--gui', '--cli'], "Action is not one of [ --gui or --cli]"
        if action == '--gui':
            gui.main()
        elif action == '--cli':
            runCLI(sys.argv[2], limit=3)
    except Exception as e:
        pass

if __name__ == '__main__':
    main()
