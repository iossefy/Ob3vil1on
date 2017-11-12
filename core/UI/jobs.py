# -*- coding: utf-8 -*-

# @author bl4ckvghost
#
# Copyright (C) 2017 Youssef Hesham
#
# License <http://www.gnu.org/licenses/gpl-3.0.html>

import sys
from PyQt4 import QtCore, QtGui
import qt
import subprocess
import os

class DO(object):
    """Just call me and i will do
       what you want me to 'DO'."""

    def about_qt(self):
        subprocess.call('python {}/core/UI/qt.py'.format(os.getcwd()), shell=True)

    def about_me(self):
        pass

    def about_script(self):
        pass

    def quit(self):
        sys.exit()

    def clear_output(self):
        pass

    def save_output(self):
        pass

    def start_cracking(self):
        pass

    def attack_method(self):
        pass

    def change_theme(self):
        pass

    def set_themes(self):
        pass

    def checks(self):
        pass
