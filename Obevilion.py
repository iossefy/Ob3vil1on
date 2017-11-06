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

def checK_py_version():
    '''checking if the python version valid'''
    req_version = '2.7.14'
    not_valid_version = '3.0.0'
    if platform.python_version()>=req_version:
        pass
    elif platform.python_version()>=not_valid_version:
        print("python %s is not supported yet\nTry the latest version of python2" % platform.python_version())
        print('Exiting...')
        time.sleep(2)
        sys.exit(1)

def check_os():
    '''Checking if the os is not linux'''
    req_os = 'posix'
    if os.name!=req_os:
        print("%s %s is not supported yet" % (platform.system(), platform.release()))
        print('Exiting...')
        time.sleep(2)
        sys.exit(1)

printer = Banner.Printer()
try:
    action = sys.argv[1]
except Exception as e:
    printer.main_banner()

def runCLI(arg1, arg2):
    Obevilion.script(path=arg1, limit=arg2)

def main():

    # Checking the required python and platform version
    check_os()
    checK_py_version()

    try:
        assert action in ['--gui', '--cli', '--help', '--about'], "Action is not one of [ --gui, --cli, --help, --about]"
        if action == '--gui':
            gui.main()
        elif action == '--cli':
            runCLI(sys.argv[2], limit=3)
        elif action == '--help':
            printer.help_banner()
        elif action == '--about':
            printer.about()
        else:
            printer.main_banner() # Just For Now
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
