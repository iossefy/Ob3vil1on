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
        '''
        Getting the path of the current directory then
        run qt.py in 'core/UI/qt.py'
        '''
        subprocess.call(
            'python {}/core/UI/qt.py'.format(os.getcwd()), shell=True)

    def about_me(self, output):
        me.main()  # Call this function
        output.append("Open About Window.")

    def about_script(self, output):
        ascript.main()  # Call this function
        output.append("Open About Script")

    def quit(self):
        '''
        Displaying a dialog window for the user
        to confirm if the user want to quit.
        '''
        root = tk.Tk()
        root.withdraw()
        answer = tk.messagebox.askquestion(
            "Quit", "Are you sure\nYou want to exit?")
        if answer == 'yes':
            sys.exit(0)
        elif answer == 'no':
            root.destroy()  # Terminating the window
            output.append("Canceled")

    def clear_output(self, output):
        output.clear()

    def start_cracking(self):
        pass

    def attack_method(self):
        pass

    def change_theme(self, theme, output):
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(theme))
        output.append("Theme Changed")
    def radioState(self, radio, field, btn):
        '''
        Checking if the BruteForce Attack radio button
        is Checked, disable the dictionary attack text
        field and dictionary attack 'choose' button,
        if not enable them.

        radio: is for the choosen radio button.
        field: is for the choosen text field.
        btn: is for the choosen 'choose' button.
        '''
        if radio.isChecked() == True:
            field.setDisabled(True)
            btn.setDisabled(True)
        elif radio.isChecked() == False:
            field.setDisabled(False)
            btn.setDisabled(False)

    def open_file(self, field, output):
        field.setText(QtGui.QFileDialog.getOpenFileName())
        output.append("Open File Chooser")
