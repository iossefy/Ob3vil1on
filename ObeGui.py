#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

class Ui_ObevilionGUI(object):
    def setupUi(self, ObevilionGUI):
        ObevilionGUI.setObjectName(_fromUtf8("ObevilionGUI"))
        ObevilionGUI.setEnabled(True)
        ObevilionGUI.resize(702, 400)
        ObevilionGUI.setMinimumSize(QtCore.QSize(600, 400))
        ObevilionGUI.setMaximumSize(QtCore.QSize(800, 400))
        ObevilionGUI.setFrameShape(QtGui.QFrame.StyledPanel)
        ObevilionGUI.setFrameShadow(QtGui.QFrame.Raised)
        self.label = QtGui.QLabel(ObevilionGUI)
        self.label.setGeometry(QtCore.QRect(0, 10, 151, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.Choose = QtGui.QPushButton(ObevilionGUI)
        self.Choose.setGeometry(QtCore.QRect(530, 10, 161, 32))
        self.Choose.setObjectName(_fromUtf8("Choose"))
        self.gridLayoutWidget = QtGui.QWidget(ObevilionGUI)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 230, 701, 171))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.textOP = QtGui.QTextEdit(self.gridLayoutWidget)
        self.textOP.setEnabled(False)
        self.textOP.setToolTip(_fromUtf8(""))
        self.textOP.setObjectName(_fromUtf8("textOP"))
        self.gridLayout.addWidget(self.textOP, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(ObevilionGUI)
        self.label_2.setGeometry(QtCore.QRect(160, 80, 351, 41))
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Impact"))
        font.setPointSize(24)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_4 = QtGui.QLabel(ObevilionGUI)
        self.label_4.setGeometry(QtCore.QRect(430, 200, 271, 21))
        self.label_4.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Impact"))
        font.setPointSize(14)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(ObevilionGUI)
        self.label_5.setGeometry(QtCore.QRect(200, 130, 261, 41))
        self.label_5.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Impact"))
        font.setPointSize(24)
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.inputText = QtGui.QTextEdit(ObevilionGUI)
        self.inputText.setGeometry(QtCore.QRect(160, 10, 351, 31))
        self.inputText.setObjectName(_fromUtf8("inputText"))
        self.pushButton = QtGui.QPushButton(ObevilionGUI)
        self.pushButton.setGeometry(QtCore.QRect(10, 190, 94, 32))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(ObevilionGUI)
        QtCore.QMetaObject.connectSlotsByName(ObevilionGUI)

    def retranslateUi(self, ObevilionGUI):
        ObevilionGUI.setWindowTitle(_translate("ObevilionGUI", "Obevilion GUI", None))
        self.label.setText(_translate("ObevilionGUI", " Enter The Archive Path", None))
        self.Choose.setText(_translate("ObevilionGUI", "Choose From Here", None))
        self.textOP.setDocumentTitle(_translate("ObevilionGUI", "OutPut", None))
        self.label_2.setText(_translate("ObevilionGUI", "Obevilion Archive Cracker", None))
        self.label_4.setText(_translate("ObevilionGUI", "https://github.com/BL4CKvGHOST/", None))
        self.label_5.setText(_translate("ObevilionGUI", "Cracks zip / rar / 7z", None))
        self.inputText.setAccessibleName(_translate("ObevilionGUI", "inputText", None))
        self.pushButton.setText(_translate("ObevilionGUI", "Crack", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ObevilionGUI = QtGui.QFrame()
    ui = Ui_ObevilionGUI()
    ui.setupUi(ObevilionGUI)
    ObevilionGUI.show()
    sys.exit(app.exec_())
