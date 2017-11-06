# -*- coding: utf-8 -*-

# @author bl4ckvghost
#
# Copyright (C) 2017 Youssef Hesham
#
# License <http://www.gnu.org/licenses/gpl-3.0.html>

from PyQt4 import QtCore, QtGui

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
    |   ---------------   =                         |
    |     .. .. .. ..           ====    ==          |
    |-----------------------------------------------|
    |                    OUTPUT                     |
    |-----------------------------------------------|

    '''
    def setupUi(self, MainWindow):
        # Setting up the window name
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        # Window size
        MainWindow.resize(800, 516)
        # Setting up the central widget
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        # Setting up the Frame size
        self.frame.setGeometry(QtCore.QRect(0, 0, 16777215, 16777214))
        self.frame.setMinimumSize(QtCore.QSize(16777214, 16777214))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        # Adding a label (Title Label)
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(310, 10, 161, 51))
        font = QtGui.QFont()
        # Setting the font
        font.setFamily(_fromUtf8("Impact"))
        font.setPointSize(28)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        # Adding a text field to the user to input
        # the Archive path
        self.archivePath = QtGui.QTextEdit(self.frame)
        self.archivePath.setGeometry(QtCore.QRect(100, 80, 501, 31))
        self.archivePath.setObjectName(_fromUtf8("archivePath"))
        # Setting up the second label
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        # Adding a PushButton to launch a filechooser
        # for the dumb user who do not know the how to
        # type the path of the encrypted archive.
        self.choose_archive = QtGui.QPushButton(self.frame)
        self.choose_archive.setGeometry(QtCore.QRect(610, 80, 94, 32))
        self.choose_archive.setObjectName(_fromUtf8("choose_archive"))
        # Setting up the third label
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 170, 131, 51))
        # Setting up the font
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Impact"))
        font.setPointSize(18)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        # Adding a checkbox to check if the user want
        # to use the bruteforce attack method.
        self.check_Bruteforce = QtGui.QCheckBox(self.frame)
        self.check_Bruteforce.setGeometry(QtCore.QRect(40, 230, 101, 25))
        self.check_Bruteforce.setObjectName(_fromUtf8("check_Bruteforce"))
        # Adding a checkbox to check if the user want to
        # user want to choose the dictionary attack method.
        self.check_dict = QtGui.QCheckBox(self.frame)
        self.check_dict.setGeometry(QtCore.QRect(40, 270, 93, 25))
        self.check_dict.setObjectName(_fromUtf8("check_dict"))
        # Setting up the fourth label
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        # Setting up second text field for the user to
        # input the path of the password list
        self.DictPath = QtGui.QTextEdit(self.frame)
        self.DictPath.setGeometry(QtCore.QRect(100, 120, 501, 31))
        self.DictPath.setObjectName(_fromUtf8("DictPath"))
        # Setting up the PushButton for the dumb user who
        # do not know how to type the path of the shity
        # password list he use.
        self.choose_dict = QtGui.QPushButton(self.frame)
        self.choose_dict.setGeometry(QtCore.QRect(610, 120, 94, 32))
        self.choose_dict.setObjectName(_fromUtf8("choose_dict"))
        # Adding a checkbox to check if the user want to use
        # symboles in the cracking process.
        self.check_Symboles = QtGui.QCheckBox(self.frame)
        self.check_Symboles.setGeometry(QtCore.QRect(200, 230, 121, 25))
        self.check_Symboles.setObjectName(_fromUtf8("check_Symboles"))
        # Check if the user is noob or not
        # Note: not all kali linux user noobs but the most of
        # them is script kiddies do not know what is the real cracking is.
        self.check_Kali = QtGui.QCheckBox(self.frame)
        self.check_Kali.setGeometry(QtCore.QRect(200, 270, 161, 25))
        self.check_Kali.setObjectName(_fromUtf8("check_Kali"))
        # Adding a PushButton to check if the noob user want to start
        # the cracking process
        self.start_cracking = QtGui.QPushButton(self.frame)
        self.start_cracking.setGeometry(QtCore.QRect(623, 280, 161, 32))
        self.start_cracking.setObjectName(_fromUtf8("start_cracking"))
        # Setting up the theme Changer for the fucken users who use
        # the fucken GUI and do not know how to use the CLI
        # and for the motherf*ckers who want to style the GUI window
        self.themeChanger = QtGui.QComboBox(self.frame)
        self.themeChanger.setGeometry(QtCore.QRect(445, 280, 161, 31))
        self.themeChanger.setObjectName(_fromUtf8("themeChanger"))
        '''
             *** Setting up the OutPut widget ***
        in the output widget there is a textbox where
             the output (Cracked Password) appear.
        '''
        # Setting up the widget
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-1, 319, 801, 181))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.output = QtGui.QTextEdit(self.widget)
        self.output.setGeometry(QtCore.QRect(0, 10, 801, 131))
        self.output.setObjectName(_fromUtf8("output"))
        MainWindow.setCentralWidget(self.centralwidget)
        # Setting up the menu bar
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuWelcome = QtGui.QMenu(self.menubar)
        self.menuWelcome.setObjectName(_fromUtf8("menuWelcome"))
        MainWindow.setMenuBar(self.menubar)
        # Setting up the status bar
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        # Setting up the menu bar components
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionHow_To_Use = QtGui.QAction(MainWindow)
        self.actionHow_To_Use.setObjectName(_fromUtf8("actionHow_To_Use"))
        self.menuWelcome.addAction(self.actionAbout)
        self.menuWelcome.addAction(self.actionQuit)
        self.menuWelcome.addAction(self.actionHow_To_Use)
        self.menubar.addAction(self.menuWelcome.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        '''
        setting up the status tip and
        setting a shortcuts for the menu bar items.
        '''
        MainWindow.setWindowTitle(_translate("MainWindow", "Obevilion", None))
        self.label.setText(_translate("MainWindow", "Obevilion", None))
        self.archivePath.setStatusTip(_translate("MainWindow", "Enter the archive path to crack", None))
        self.label_2.setText(_translate("MainWindow", "Arhive Path", None))
        self.choose_archive.setStatusTip(_translate("MainWindow", "Choose archive from file system", None))
        self.choose_archive.setText(_translate("MainWindow", "Choose", None))
        self.label_3.setText(_translate("MainWindow", "What To Use", None))
        self.check_Bruteforce.setStatusTip(_translate("MainWindow", "Use bruteforce attack method", None))
        self.check_Bruteforce.setText(_translate("MainWindow", "BruteForce", None))
        self.check_dict.setStatusTip(_translate("MainWindow", "Use dictionary attack method", None))
        self.check_dict.setText(_translate("MainWindow", "Dictionary", None))
        self.label_4.setText(_translate("MainWindow", "Dictionary", None))
        self.DictPath.setStatusTip(_translate("MainWindow", "Enter the path of the password list", None))
        self.choose_dict.setStatusTip(_translate("MainWindow", "Choose password list from file system", None))
        self.choose_dict.setText(_translate("MainWindow", "Choose", None))
        self.check_Symboles.setStatusTip(_translate("MainWindow", "Use Symboles in the cracking process", None))
        self.check_Symboles.setText(_translate("MainWindow", "Use Symboles", None))
        self.check_Kali.setStatusTip(_translate("MainWindow", "Check if you are using kali linux", None))
        self.check_Kali.setText(_translate("MainWindow", "Use External Scripts", None))
        self.start_cracking.setStatusTip(_translate("MainWindow", "Begin The Cracking Process", None))
        self.start_cracking.setText(_translate("MainWindow", "Lets Go!", None))
        self.themeChanger.setStatusTip(_translate("MainWindow", "Change The Window Theme", None))
        self.widget.setStatusTip(_translate("MainWindow", "The output shows here", None))
        self.menuWelcome.setTitle(_translate("MainWindow", "Obevilion", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionAbout.setStatusTip(_translate("MainWindow", "About The Programmer", None))
        self.actionAbout.setShortcut(_translate("MainWindow", "Ctrl+B", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionQuit.setStatusTip(_translate("MainWindow", "Close the application", None))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionHow_To_Use.setText(_translate("MainWindow", "How To Use?", None))
        self.actionHow_To_Use.setStatusTip(_translate("MainWindow", "How to use Obevilion", None))
        self.actionHow_To_Use.setShortcut(_translate("MainWindow", "Ctrl+H", None))


def main():
    '''Main Method'''
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
