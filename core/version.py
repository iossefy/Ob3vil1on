# -*- coding: utf-8 -*-

# @author bl4ckvghost
#
# Copyright (C) 2017 Youssef Hesham
#
# License <http://www.gnu.org/licenses/gpl-3.0.html>

"""
Getting Ob3vil1on version from this script.
it scrap version file from github then compare it
with the local version.
"""

import platform
import sys
import os
from Banner import Printer
import writer

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
                data = check_version.read().strip()  # Reading the file content
                response = urlopen(  # Updated version of the file
                    'https://raw.githubusercontent.com/BL4CKvGHOST/Ob3vil1on/master/core/configuration/version.txt')
                version = response.read().decode('utf-8').strip()
                if version != data:  # if the online version not equal the local version
                    print(writer.red("current is {} there is new version available: {}".format(
                        data, version), bold=True))
                else:
                     # if the online version equal the local version
                    print(writer.green(
                        "You are using the latest version:{}".format(data), bold=True))
        except Exception as e:
            printer.unknowen_error(e)

    def current(self):
        """
        Getting the current version
        """
        try:
            with open('core/configuration/version.txt', 'r') as current_version:
                data = current_version.read().strip()  # Read the current version
            print(writer.green("Current Version Is: {}".format(
                data), bold=True))  # Print Version
        except Exception as e:
            printer.unknowen_error(e)

    def vManage(self, variable):
        """
        Managing User Input Terminal Args
        """
        if variable == "--check":
            self.check_for_updates()  # Run This Method
        elif variable == '--current':
            self.current()  # Run This Method
        else:
            # print invalid input + {variable}
            print("Invalid Input {}".format(variable))
