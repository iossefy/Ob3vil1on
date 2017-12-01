# -*- coding: utf-8 -*-

# @author bl4ckvghost
#
# Copyright (C) 2017 Youssef Hesham
#
# License <http://www.gnu.org/licenses/gpl-3.0.html>

import platform
import sys
import os
from Banner import Printer

printer = Printer()

if platform.python_version()[0] == '2':
    from urllib import urlopen
elif platform.python_version()[0] == '3':
    from urllib.request import urlopen
else:
    print("WTF!, unknowen python version!")
    sys.exit(-1)


class VControl(object):
    """docstring for VControl."""

    def check_for_updates(self):
        try:
            with open('core/configuration/version.txt', 'r') as check_version:
                data = check_version.read().strip()
                response = urlopen(
                    'https://raw.githubusercontent.com/BL4CKvGHOST/Obevilion/master/core/configuration/version.txt')
                version = response.read().decode('utf-8').strip()
                if version != data:
                    print("current is {} there is new version available: {}".format(
                        data, version))
                else:
                    print("You are using the latest version:{}".format(data))
        except Exception as e:
            printer.unknowen_error(e)

    def current(self):
        try:
            with open('core/configuration/version.txt', 'r') as current_version:
                data = current_version.read().strip()
            print("Current Version Is: {}".format(data))
        except Exception as e:
            printer.unknowen_error(e)

    def vManage(self, variable):
        if variable == "--check":
            self.check_for_updates()
        elif variable == '--current':
            self.current()
        else:
            print("Invalid Input {}".format(variable))
