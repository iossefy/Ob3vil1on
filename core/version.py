# -*- coding: utf-8 -*-

# @author bl4ckvghost
#
# Copyright (C) 2017 Youssef Hesham
#
# License <http://www.gnu.org/licenses/gpl-3.0.html>

import platform
import sys
import os

version = None

if platform.python_version()[0] == '2':
    from urllib import urlopen
elif platform.python_version()[0] == '3':
    from urllib.request import urlopen
else:
    print("WTF!, unknowen python version!")
    sys.exit(-1)


def check_for_updates():
    with open(os.path.join('core/configuration', 'version.txt'), 'r') as check_version:
        data = check_version.read.strip()
        try:
            response = urlopen(
                'https://raw.githubusercontent.com/BL4CKvGHOST/Obevilion/master/core/configuration/version.txt')
        except Exception as e:
            return data
        version = response.read().decode('utf-8').strip()
        if version != data:
            return data + " there is new version available: " + version
        else:
            return "You are using the latest version: " + data


def current():
    with open(os.path.join('core/configuration', 'version.txt'), 'r') as current_version:
        data = current_version.read.strip()
    return "Version: " + data
