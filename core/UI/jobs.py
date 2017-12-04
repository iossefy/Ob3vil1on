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

    def about_qt(self, output):
        '''
        Getting the path of the current directory then
        run qt.py in 'core/UI/qt.py'
        '''
        try:
            subprocess.call(
                'python {}/core/UI/qt.py'.format(os.getcwd()), shell=True)
            output.append("Open About Qt")
        except Exception as e:
            output.append(e)

    def about_me(self, output):
        try:
            me.main()  # Call this function
            output.append("Open About Window.")
        except Exception as e:
            output.append(e)

    def about_script(self, output):
        try:
            ascript.main()  # Call this function
            output.append("Open About Script")
        except Exception as e:
            output.append(e)

    def quit(self, output=None):
        '''
        Displaying a dialog window for the user
        to confirm if the user want to quit.
        '''
        try:
            root = tk.Tk()
            root.withdraw()
            answer = tk.messagebox.askquestion(
                "Quit", "Are you sure\nYou want to exit?")
            if answer == 'yes':
                sys.exit(0)
            elif answer == 'no':
                root.destroy()  # Terminating the window
                if output != None:
                    output.append("Quit action canceled by user")
                else:
                    pass
        except Exception as e:
            output.append(e)

    def clear_output(self, output):
        try:
            output.clear()
        except Exception as e:
            output.append(e)

    def start_cracking(self):
        pass

    def bruteforce(self, path, textField):
        pass

    def dictionary(self, path, textField, dict):
        pass

    def change_theme(self, theme, output):
        try:
            QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(theme))
            output.append("Theme Changed")
        except Exception as e:
            output.append(e)

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
        try:
            if radio.isChecked() == True:
                field.setDisabled(True)
                btn.setDisabled(True)
            elif radio.isChecked() == False:
                field.setDisabled(False)
                btn.setDisabled(False)
        except Exception as e:
            output.append(e)

    def open_file(self, field, output):
        try:
            field.setText(QtGui.QFileDialog.getOpenFileName())
            output.append("Open File Chooser")
        except Exception as e:
            output.append(e)
