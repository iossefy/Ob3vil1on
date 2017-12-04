# -*- coding: utf-8 -*-

# @author bl4ckvghost
#
# Copyright (C) 2017 Youssef Hesham
#
# License <http://www.gnu.org/licenses/gpl-3.0.html>

"""
***WHAT IS THIS ALL ABOUT?***
Checking all is ok before starting the script
"""

import os
import sys
import platform
import shutil
import time


class Check_req:
    """Checking The Requirments to run the app."""

    def check_py_version(self):
        '''checking if the python version valid.
           python3 is not supported at the main script.
           but it requires when running the attacking script.
           you must have both'''

        req_version = '2.7.14'
        not_valid_version = '3.0.0'
        if platform.python_version() >= req_version:
            pass
        elif platform.python_version() >= not_valid_version:
            print("python %s is not supported yet\nTry the latest version of python2" %
                  platform.python_version())
            print('Exiting...')
            time.sleep(2)
            sys.exit(1)

    def check_softwares(self):
        '''Check if the user installed all the required packages.

           Python: Required to run the main script.
           python3: Required to run the model script (Attacking Script).
           unrar: Required to check the password of the archive
           p7zip: Required to check the password of the archive, works as unrar

           [Information]p7zip and unrar is created to create archives and unpack it
           with the extension of zip, 7z and rar.'''

        for which in ["unrar", "p7zip", "7z"]:
            if not shutil.which(which):
                print("ERROR: %s isn't installed." % which)
                print("Exiting...")
                sys.exit(1)

    def check_os(self):
        '''Checking if the os is not linux.
           if not linux, do not run :)'''

        req_os = 'posix'
        if os.name != req_os:
            print("%s %s is not supported yet" %
                  (platform.system(), platform.release()))
            print('Exiting...')
            time.sleep(2)
            sys.exit(1)

    def check_user(self):
        if not os.geteuid() == 0:
            print("Script must run as root!")
            time.sleep(0.6)
            sys.exit(0)
