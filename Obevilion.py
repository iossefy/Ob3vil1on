# -*- coding: utf-8 -*-

# @author bl4ckvghost
#
# Copyright (C) 2017 Youssef Hesham
#
# License <http://www.gnu.org/licenses/gpl-3.0.html>

import sys
import os
import subprocess
from core import Banner, Obevilion, Check, Control
from core.UI import gui

check_req = Check.Check_req()
printer = Banner.Printer()
looprocess = Control.LoopControl()
action = ''
commands = ['--gui', '--cli', '--help', '--about',
            '--easy_mode', '--about_me', '--license']


def get_name(arg=''):
    '''
    Managing the file name
    '''
    name = os.path.basename(__file__)
    if arg == 'noPy':
        return name.replace('.py', '')
    elif arg == 'all':
        if 'pyc' not in name:
            return name
        elif 'pyc' in name:
            return name.replace('.pyc', '')
        elif 'py' in name:
            return name.replace('.py', '')
        else:
            return None
    elif arg == '':
        if "pyc" not in name:
            return name
        else:
            return name.replace('pyc', 'py')
        return None


try:
    action = sys.argv[1]
except Exception as e:
    printer.main_banner()


def loop_action(action):  # Using the easy loop system
    if action == '--easy_mode':
        printer.main_banner
        looprocess.loop()
    else:
        pass


def main():

    check_req.check_os()  # Checking the required operation system
    check_req.check_py_version()  # Check valid python version
#    check_req.check_softwares() # Checking if the user have the required softwares
    looprocess.main_loop(action=action, commands=commands)  # Run


if __name__ == '__main__':
    main()
