# -*- coding: utf-8 -*-

# @author bl4ckvghost
#
# Copyright (C) 2017 Youssef Hesham
#
# License <http://www.gnu.org/licenses/gpl-3.0.html>

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
import os

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


class Ui_AboutQT(object):
    def setupUi(self, AboutQT):
        AboutQT.setObjectName(_fromUtf8("AboutQT"))
        AboutQT.resize(611, 436)
        AboutQT.setFrameShape(QtGui.QFrame.StyledPanel)
        AboutQT.setFrameShadow(QtGui.QFrame.Raised)
        self.label = QtGui.QLabel(AboutQT)
        self.label.setGeometry(QtCore.QRect(8, 0, 71, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(AboutQT)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 201, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(AboutQT)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 461, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(AboutQT)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 581, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(AboutQT)
        self.label_5.setGeometry(QtCore.QRect(10, 110, 521, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(AboutQT)
        self.label_6.setGeometry(QtCore.QRect(10, 140, 581, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(AboutQT)
        self.label_7.setGeometry(QtCore.QRect(10, 160, 131, 20))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(AboutQT)
        self.label_8.setGeometry(QtCore.QRect(10, 190, 561, 20))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(AboutQT)
        self.label_9.setGeometry(QtCore.QRect(10, 210, 601, 20))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(AboutQT)
        self.label_10.setGeometry(QtCore.QRect(10, 230, 511, 20))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(AboutQT)
        self.label_11.setGeometry(QtCore.QRect(10, 260, 521, 20))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(AboutQT)
        self.label_12.setGeometry(QtCore.QRect(10, 280, 571, 20))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(AboutQT)
        self.label_13.setGeometry(QtCore.QRect(10, 300, 71, 20))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(AboutQT)
        self.label_14.setGeometry(QtCore.QRect(10, 330, 411, 20))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(AboutQT)
        self.label_15.setGeometry(QtCore.QRect(10, 350, 391, 20))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(AboutQT)
        self.label_16.setGeometry(QtCore.QRect(10, 380, 591, 20))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_17 = QtGui.QLabel(AboutQT)
        self.label_17.setGeometry(QtCore.QRect(10, 400, 81, 20))
        self.label_17.setObjectName(_fromUtf8("label_17"))

        self.retranslateUi(AboutQT)
        QtCore.QMetaObject.connectSlotsByName(AboutQT)

    def retranslateUi(self, AboutQT):
        AboutQT.setWindowTitle(_translate("AboutQT", "About Qt", None))
        self.label.setText(_translate("AboutQT", "About Qt", None))
        self.label_2.setText(_translate(
            "AboutQT", "This program uses Qt version 4", None))
        self.label_3.setText(_translate("AboutQT", "Qt is a C++, Python toolkit for cross-platform application development.\n"
                                        "", None))
        self.label_4.setText(_translate(
            "AboutQT", "Qt provides single-source portability across all major desktop operating systems. It is also", None))
        self.label_5.setText(_translate(
            "AboutQT", "available for embedded Linux and other embedded and mobile operating systems.", None))
        self.label_6.setText(_translate(
            "AboutQT", "Qt is available under three different licensing options designed to accommodate the needs", None))
        self.label_7.setText(_translate(
            "AboutQT", "of our various users.", None))
        self.label_8.setText(_translate(
            "AboutQT", "Qt licensed under our commercial license agreement is appropriate for development of", None))
        self.label_9.setText(_translate(
            "AboutQT", "proprietary/commercial software where you do not want to share any source code with third", None))
        self.label_10.setText(_translate(
            "AboutQT", "parties or otherwise cannot comply with the terms of the GNU LGPL version 3.", None))
        self.label_11.setText(_translate(
            "AboutQT", "Qt licensed under the GNU LGPL version 3 is appropriate for the development of", None))
        self.label_12.setText(_translate(
            "AboutQT", "Qt applications provided you can comply with the terms and conditions of the GNU LGPL", None))
        self.label_13.setText(_translate("AboutQT", "version 3.", None))
        self.label_14.setText(_translate(
            "AboutQT", "Copyright (C) 2016 The Qt Company Ltd and other contributors", None))
        self.label_15.setText(_translate(
            "AboutQT", "Qt and the Qt logo are trademarks of The Qt Company Ltd.", None))
        self.label_16.setText(_translate(
            "AboutQT", "Qt is The Qt Company Ltd product developed as an open source project. See qt.io for more", None))
        self.label_17.setText(_translate("AboutQT", "information.", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    AboutQT = QtGui.QFrame()
    ui = Ui_AboutQT()
    ui.setupUi(AboutQT)
    AboutQT.show()
    sys.exit(app.exec_())
