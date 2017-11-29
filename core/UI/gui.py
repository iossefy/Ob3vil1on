# -*- coding: utf-8 -*-

# @author bl4ckvghost
#
# Copyright (C) 2017 Youssef Hesham
#
# License <http://www.gnu.org/licenses/gpl-3.0.html>

import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from jobs import DO

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.do = DO()
        '''
        Implementing the window in this class
        in this class Implementing the whole window
        like setting up the window theme manager,
        setting up the buttons and the text fields
        to use it in cracking process, setting up
        the labels and the size of the window and more!.


                  Creating a Window Like this
        |-----------------------------------------------|
        |                   Obevilion                   |
        |-----------------------------------------------|
        |                                               |
        |   ---------------   =                         |
        |   ---------------   =             =======  == |
        |     .. .. .. ..                   ==   ==  == |
        |-----------------------------------------------|
        |                    OUTPUT                     |
        |-----------------------------------------------|

        '''

        # Set window object name
        MainWindow.setObjectName(_fromUtf8("MainWindow"))

        # set window size
        MainWindow.setFixedSize(800, 516)

        # setting up the central widget
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        # Setting up the frame
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 16777215, 16777214))
        self.frame.setMinimumSize(QtCore.QSize(16777214, 16777214))
        self.frame.setStatusTip(_fromUtf8(""))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))

        # Setting up the label1
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(310, 10, 161, 51))

        # setting up the font
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Impact"))
        font.setPointSize(28)
        font.setItalic(True)

        # applying the font to the label
        self.label.setFont(font)
        self.label.setText(_fromUtf8("Obevilion"))
        self.label.setObjectName(_fromUtf8("label"))

        # setting up the textfield to input archive path
        self.archivePath = QtGui.QTextEdit(self.frame)
        self.archivePath.setGeometry(QtCore.QRect(100, 80, 501, 31))
        self.archivePath.setObjectName(_fromUtf8("archivePath"))

        # Setting up the label_2
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 81, 31))

        # setting up the font
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        # setting up a button to choose archive easily
        self.choose_archive = QtGui.QPushButton(self.frame)
        self.choose_archive.setGeometry(QtCore.QRect(610, 80, 94, 32))
        self.choose_archive.setObjectName(_fromUtf8("choose_archive"))
        self.choose_archive.clicked.connect(
            lambda: self.do.open_file(self.archivePath, self.output))

        # settong up label_3
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 180, 131, 51))

        # Setting up the font
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Impact"))
        font.setPointSize(18)
        font.setItalic(True)

        self.label_3.setFont(font)
        self.label_3.setText(_fromUtf8("What To Use"))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        # Setting up label_4
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 81, 31))

        font = QtGui.QFont()
        font.setPointSize(12)

        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))

        # Setting up a textfield to input the Dictionary path
        self.DictPath = QtGui.QTextEdit(self.frame)
        self.DictPath.setGeometry(QtCore.QRect(100, 120, 501, 31))
        self.DictPath.setObjectName(_fromUtf8("DictPath"))

        # Setting up a button to open filechooser to choose the dictionary path
        self.choose_dict = QtGui.QPushButton(self.frame)
        self.choose_dict.setGeometry(QtCore.QRect(610, 120, 94, 32))
        self.choose_dict.setObjectName(_fromUtf8("choose_dict"))
        self.choose_dict.clicked.connect(
            lambda: self.do.open_file(self.DictPath, self.output))

        #######################################################################
        # # use Symboles in cracking ######################### OLD CODE #######
        # self.check_Symboles = QtGui.QCheckBox(self.frame)  ##################
        # self.check_Symboles.setGeometry(QtCore.QRect(180, 250, 121, 25))    #
        # self.check_Symboles.setObjectName(_fromUtf8("check_Symboles"))      #
        #                                                                     #
        # # use kali linux tools                                              #
        # self.check_Kali = QtGui.QCheckBox(self.frame)                       #
        # self.check_Kali.setGeometry(QtCore.QRect(180, 290, 161, 25))        #
        # self.check_Kali.setObjectName(_fromUtf8("check_Kali"))              #
        #######################################################################

        # Setting up the start cracking button
        self.start_cracking = QtGui.QPushButton(self.frame)
        self.start_cracking.setGeometry(QtCore.QRect(600, 290, 190, 32))
        self.start_cracking.setObjectName(_fromUtf8("start_cracking"))

        # Setting up the theme changer
        self.theme_changer = QtGui.QComboBox(self.frame)
        # Setting up the combo box items
        self.themes = ["motif", "windows", "cde",
                       "Plastique", "Cleanlooks", "gtk+"]
        self.theme_changer.addItems(self.themes)
        # self.theme_changer.activated[str].connect(self.do.change_theme)
        self.theme_changer.setGeometry(QtCore.QRect(500, 250, 191, 31))
        self.theme_changer.setObjectName(_fromUtf8("theme_changer"))

        # BruteForce Attack radio button
        self.check_bruteforce = QtGui.QRadioButton(self.frame)
        self.check_bruteforce.setGeometry(QtCore.QRect(20, 250, 109, 25))
        self.check_bruteforce.setObjectName(_fromUtf8("check_bruteforce"))
        self.check_bruteforce.toggled.connect(lambda: self.do.radioState(self.check_bruteforce,
                                                                         self.DictPath, self.choose_dict))
        self.check_bruteforce.setChecked(True)

        # Dictionary Attack radio button
        self.check_dict = QtGui.QRadioButton(self.frame)
        self.check_dict.setGeometry(QtCore.QRect(20, 290, 109, 25))
        self.check_dict.setObjectName(_fromUtf8("check_dict"))

        # Button to save the output in a txt file
        # self.save_output = QtGui.QPushButton(self.frame)
        # self.save_output.setGeometry(QtCore.QRect(600, 290, 94, 32))
        # self.save_output.setObjectName(_fromUtf8("save_output"))

        # Clear the output from the output textfield
        self.clear_output = QtGui.QPushButton(self.frame)
        self.clear_output.setGeometry(QtCore.QRect(500, 290, 94, 32))
        self.clear_output.setObjectName(_fromUtf8("clear_output"))
        self.clear_output.clicked.connect(
            lambda: self.do.clear_output(self.output))

        # Setting up a button to Apply the choosed theme
        self.apply_theme = QtGui.QPushButton(self.frame)
        self.apply_theme.setGeometry(QtCore.QRect(700, 250, 91, 32))
        self.apply_theme.setObjectName(_fromUtf8("apply_theme"))
        self.apply_theme.clicked.connect(
            lambda: self.do.change_theme(str(self.theme_changer.currentText()), self.output))

        # Setting up the label_5
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(470, 180, 151, 51))

        # Setting up the font
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Impact"))
        font.setPointSize(18)
        font.setItalic(True)

        self.label_5.setFont(font)
        self.label_5.setText(_fromUtf8("Options"))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        # Setting up the output widget
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-1, 319, 801, 181))
        self.widget.setObjectName(_fromUtf8("widget"))

        self.output = QtGui.QTextEdit(self.widget)
        self.output.setGeometry(QtCore.QRect(0, 10, 801, 131))
        self.output.setObjectName(_fromUtf8("output"))
        MainWindow.setCentralWidget(self.centralwidget)
        # self.save_output.clicked.connect(
        #     lambda: self.do.save_output(self.output))

        # Setting up the menubar
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))

        self.menuWelcome = QtGui.QMenu(self.menubar)
        self.menuWelcome.setObjectName(_fromUtf8("menuWelcome"))

        self.about = QtGui.QMenu(self.menuWelcome)
        self.about.setObjectName(_fromUtf8("about"))
        MainWindow.setMenuBar(self.menubar)

        # Setting up the status bar
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionQuit.triggered.connect(lambda: self.do.quit(output=self.output))

        self.about_me = QtGui.QAction(MainWindow)
        self.about_me.setObjectName(_fromUtf8("about_me"))
        self.about_me.triggered.connect(lambda: self.do.about_me(self.output))

        self.about_obevilion = QtGui.QAction(MainWindow)
        self.about_obevilion.setObjectName(_fromUtf8("about_obevilion"))
        self.about_obevilion.triggered.connect(
            lambda: self.do.about_script(self.output))

        self.about_qt = QtGui.QAction(MainWindow)
        self.about_qt.setObjectName(_fromUtf8("about_qt"))
        self.about_qt.triggered.connect(lambda: self.do.about_qt(self.output))

        self.about.addAction(self.about_me)
        self.about.addAction(self.about_obevilion)
        self.about.addAction(self.about_qt)

        self.menuWelcome.addAction(self.about.menuAction())
        self.menuWelcome.addAction(self.actionQuit)
        self.menubar.addAction(self.menuWelcome.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Obevilion", None))
        self.archivePath.setStatusTip(_translate(
            "MainWindow", "Enter the archive path to crack", None))

        self.label_2.setText(_translate("MainWindow", "Archive", None))
        self.choose_archive.setStatusTip(_translate(
            "MainWindow", "Choose archive from file system", None))
        self.choose_archive.setText(_translate("MainWindow", "Browse", None))

        self.label_4.setText(_translate("MainWindow", "Dictionary", None))
        self.DictPath.setStatusTip(_translate(
            "MainWindow", "Enter the path of the password list", None))

        self.choose_dict.setStatusTip(_translate(
            "MainWindow", "Choose password list from file system", None))
        self.choose_dict.setText(_translate("MainWindow", "Browse", None))

        self.start_cracking.setStatusTip(_translate(
            "MainWindow", "Begin The Cracking Process", None))
        self.start_cracking.setText(_translate("MainWindow", "Let's Do It", None))

        self.theme_changer.setStatusTip(
            _translate("MainWindow", "Theme changer", None))

        self.check_bruteforce.setStatusTip(_translate(
            "MainWindow", "Use Bruteforce attack", None))
        self.check_bruteforce.setText(
            _translate("MainWindow", "BruteForce", None))
        self.check_dict.setStatusTip(_translate(
            "MainWindow", "Use dictionary attack", None))
        self.check_dict.setText(_translate("MainWindow", "Dictionary", None))

        # self.save_output.setStatusTip(_translate(
        #     "MainWindow", "Save the output to a text file", None))
        # self.save_output.setText(_translate("MainWindow", "Save output", None))

        self.clear_output.setStatusTip(_translate(
            "MainWindow", "Clear the output from the screen", None))
        self.clear_output.setText(_translate(
            "MainWindow", "Clear output", None))

        self.apply_theme.setStatusTip(_translate(
            "MainWindow", "Apply the choosed theme", None))
        self.apply_theme.setText(_translate("MainWindow", "Apply", None))

        self.widget.setStatusTip(_translate(
            "MainWindow", "The output shows here", None))
        self.menuWelcome.setTitle(_translate("MainWindow", "Obevilion", None))
        self.about.setTitle(_translate("MainWindow", "About", None))

        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionQuit.setStatusTip(_translate(
            "MainWindow", "Close the application", None))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))

        self.about_me.setText(_translate("MainWindow", "About Me", None))
        self.about_me.setStatusTip(_translate("MainWindow", "About Me", None))

        self.about_obevilion.setText(_translate(
            "MainWindow", "About Obevilion", None))
        self.about_obevilion.setStatusTip(
            _translate("MainWindow", "About Obevilion", None))

        self.about_qt.setText(_translate("MainWindow", "About Qt", None))
        self.about_qt.setStatusTip(_translate("MainWindow", "About Qt", None))


def main():
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
