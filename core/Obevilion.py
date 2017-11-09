# -*- coding: utf-8 -*-

# @author bl4ckvghost
#
# Copyright (C) 2017 Youssef Hesham
#
# License <http://www.gnu.org/licenses/gpl-3.0.html>

# Import The Needed Lib
import time
import os
import sys
import shutil
import itertools
import Banner

def get_name(arg=''):
    '''
    Managing the file name
    '''
    name = os.path.basename(__file__)
    if arg=='noPy':
        return name.replace('.py', '')
    elif arg=='all':
        if 'pyc' not in name:
            return name
        elif 'pyc' in name:
            return name.replace('.pyc', '')
        elif 'py' in name:
            return name.replace('.py', '')
        else:
            return None
    elif arg=='':
        if "pyc" not in name:
            return name
        else:
            return name.replace('pyc','py')
        return None
