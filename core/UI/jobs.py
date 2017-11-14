# -*- coding: utf-8 -*-

# @author bl4ckvghost
#
# Copyright (C) 2017 Youssef Hesham
#
# License <http://www.gnu.org/licenses/gpl-3.0.html>

from PyQt4 import QtCore, QtGui
import qt
import os
import me
import ascript
import sys
import subprocess
import tkinter as tk
import tkinter.messagebox

class DO(object):
    """Just call me and i will do
       what you want me to 'DO'."""

    def about_qt(self):
        subprocess.call('python {}/core/UI/qt.py'.format(os.getcwd()), shell=True)

    def about_me(self):
        me.main()

    def about_script(self):
        ascript.main()

    def quit(self):
        root = tk.Tk()
        root.withdraw()
        answer = tk.messagebox.askquestion("Quit", "Are you sure\nYou want to exit?")
        if answer == 'yes':
            sys.exit(0)
        elif answer == 'no':
            root.destroy()

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

    def radioState(self, radio, field, btn):
        if radio.isChecked() == True:
            field.setDisabled(True)
            btn.setDisabled(True)
        elif radio.isChecked() == False:
            field.setDisabled(False)
            btn.setDisabled(False)

    def open_file(self, field):
        field.setText(QtGui.QFileDialog.getOpenFileName())
