# -*- coding: utf-8 -*-
import os
import sys
import platform
from core import Banner, gui, Obevilion

printer = Banner.Printer()
action = sys.argv[1]

def runCLI(arg):
    if arg is not None:
        Obevilion.script(path=arg, limit=3)
    else:
        printer.main_banner()

def main():

    assert action in ['--gui', '--cli'], "Action is not one of [ --gui or --cli]"
    if action == '--gui':
        gui.main()
    elif action == '--cli':
        runCLI(sys.argv[2])

if __name__ == '__main__':
    main()
