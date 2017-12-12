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
import attack
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
                'python {}/core/UI/qt.py'.format(os.getcwd()), shell=True)  # Call qt.py script
            output.append("Open About Qt")  # Logging to the console
        except Exception as e:
            output.append(str(e))

    def about_me(self, output):
        try:
            me.main()  # Call this function
            output.append("Open About Window.")
        except Exception as e:
            output.append(str(e))

    def about_script(self, output):
        """
        Calling about the script.
        this script runs ascript.py
        """
        try:
            ascript.main()  # Call this function
            output.append("Open About Script")
        except Exception as e:
            output.append(str(e))

    def quit(self, output=None):
        '''
        Displaying a dialog window for the user
        to confirm if the user want to quit.
        '''
        try:
            root = tk.Tk()  # root window
            root.withdraw()
            # Ask a question
            answer = tk.messagebox.askquestion(
                "Quit", "Are you sure\nYou want to exit?")
            if answer == 'yes':  # if the user said yes
                sys.exit(0)
            elif answer == 'no':  # if the user said no
                root.destroy()  # Terminating the window
                if output != None:
                    # Logging to the console
                    output.append("Quit action canceled by user")
                else:
                    pass
        except Exception as e:
            output.append(str(e))

    def clear_output(self, output):
        """Clear the output"""
        try:
            output.clear()  # Clear output console
        except Exception as e:
            output.append(str(e))

    def start_cracking(self, radio, textField, path=None, passlist=None):
        """
        The main function to manage cracking methods (BruteForce / Dictionary) Attacks.

        Parameters:
        radio: this will be the bruteforce radio by default.
        textField: the output textfield that the password display on.
        path: the path of archive file.
        passlist: (optional) for dictionary attack.
        """
        try:
            if path == '' or path is None:
                textField.append("Path messing!")
            if radio.isChecked() == True:
                if os.path.exists(path):
                    if path[-4:] == '.zip' or path[-4:] == '.rar' or path[-3:] == '.7z':
                        self.bruteforce(path, textField)
                    else:
                        textField.append(
                            "File is not supported. Cracking [zip/rar/7z] only")
                else:
                    textField.append(
                        "File Not Found!, check if the path exist")
            else:
                try:
                    if path == '' or path is None:
                        textField.append("Path messing!")
                    elif passlist == '' or passlist is None:
                        textField.append("passlist messing!")
                    else:
                        if path[-4:] == '.zip' or path[-4:] == '.rar' or path[-3:] == '.7z':
                            if os.path.exists(path):
                                self.dictionary(path, textField, passlist)
                            else:
                                textField.append(
                                    "File Not Found!, check if the path exist")
                        else:
                            textField.append(
                                "File is not supported. Cracking [zip/rar/7z] only")
                except Exception as e:
                    textField.append(str(e))
        except Exception as e:
            textField.append(str(e))

    def bruteforce(self, path, textField):
        """
        Bruteforce attack code goes here.
        path: path of the target Archive File.
        textField: the output textfield.
        """
        try:
            attack.rc(path, textField)
        except Exception as e:
            textField.append(str(e))

    def dictionary(self, path, textField, passlist):
        """
        Dictionary attack code goes here.
        path: path of the target Archive File.
        textField: the output textfield.
        passlist: password list to iterate on.
        """
        try:
            textField.append("Not Available Right Now!")
        except Exception as e:
            textField.append(str(e))

    def change_theme(self, theme, output):
        """
        Changing The Theme.
        The user can choose from the following themes,

        ["motif", "windows", "cde",
        "Plastique", "Cleanlooks", "gtk+"]
        """
        try:
            QtGui.QApplication.setStyle(
                QtGui.QStyleFactory.create(theme))  # Changing the theme
            output.append("Theme Changed")  # Logging to the console
        except Exception as e:
            output.append(str(e))

    def radioState(self, radio, field, btn, output):
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
            if radio.isChecked() == True:  # if the radio button is checked
                field.setDisabled(True)  # disable text field
                btn.setDisabled(True)  # disable button
                output.append("Bruteforce attack enabled")
            elif radio.isChecked() == False:  # if the radio button is not checked
                field.setDisabled(False)  # enable text field
                btn.setDisabled(False)  # enable button
                # Logging to the console
                output.append("Dictionary attack enabled")
        except Exception as e:
            output.append(str(e))

    def open_file(self, field, output):
        """
        Open file dialog to let the user choose the
        file easily without entering it manualy.
        """
        try:
            field.setText(QtGui.QFileDialog.getOpenFileName())
            output.append("choosed: {}".format(field.toPlainText()))
        except Exception as e:
            output.append(str(e))
