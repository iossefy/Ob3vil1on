# -*- coding: utf-8 -*-

# @author bl4ckvghost
#
# Copyright (C) 2017 Youssef Hesham
#
# License <http://www.gnu.org/licenses/gpl-3.0.html>

import sys
import subprocess
from core import Banner, Obevilion, Check, Control
from core.UI import gui

check_req  = Check.Check_req()
printer    = Banner.Printer()
looprocess = Control.LoopControl()

action = ''
commands = ['--gui', '--cli', '--help', '--about', '--easy_mode', '--about_me', '--license']

try:
    action = sys.argv[1]
except Exception as e:
    printer.main_banner()
    # looprocess.loop()

def loop_action(action): # Using the easy loop system
    if action == '--easy_mode':
        printer.main_banner
        looprocess.loop()
    else:
        pass

def run():
    try:
        assert action in commands, "Action is not one of %s" % ', '.join(map(str, commands))
        try:
            if action == '--easy_mode':
                subprocess.call('clear', shell=True)
                printer.main_banner()
                loop_action(action)
            else:
                pass
        except Exception as e:
            pass
        if action == '--gui':
            gui.main()
        elif action == '--cli':
            print("Not Working Right Now")
        elif action == '--help':
            printer.help_banner()
        elif action == '--about':
            printer.about()
        elif action == '--about_me':
            printer.about_me()
        elif action == '--license':
            printer.License()
    except Exception as e:
        try:
            if sys.argv[1] is not commands:
                printer.invalid_input()
            else:
                pass
        except Exception as e:
            pass

def main():

    check_req.check_os() # Checking the required operation system
    check_req.check_py_version() # Check valid python version
    run() # Run

if __name__ == '__main__':
    main()
