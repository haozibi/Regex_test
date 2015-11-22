# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'three.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

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

class Ui_bzizi(object):
    def setupUi(self, bzizi):
        bzizi.setObjectName(_fromUtf8("bzizi"))
        bzizi.resize(712, 463)
        bzizi.setMinimumSize(QtCore.QSize(712, 463))
        bzizi.setMaximumSize(QtCore.QSize(712, 463))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("ico.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        bzizi.setWindowIcon(icon)
        self.text_regex = QtGui.QTextEdit(bzizi)
        self.text_regex.setGeometry(QtCore.QRect(20, 50, 551, 75))
        self.text_regex.setObjectName(_fromUtf8("text_regex"))
        self.text_data = QtGui.QTextEdit(bzizi)
        self.text_data.setGeometry(QtCore.QRect(20, 170, 331, 271))
        self.text_data.setObjectName(_fromUtf8("text_data"))
        self.text_show = QtGui.QTextBrowser(bzizi)
        self.text_show.setGeometry(QtCore.QRect(380, 170, 311, 271))
        self.text_show.setObjectName(_fromUtf8("text_show"))
        self.button_ok = QtGui.QPushButton(bzizi)
        self.button_ok.setGeometry(QtCore.QRect(600, 50, 85, 27))
        self.button_ok.setObjectName(_fromUtf8("button_ok"))
        self.button_about = QtGui.QPushButton(bzizi)
        self.button_about.setGeometry(QtCore.QRect(600, 100, 85, 27))
        self.button_about.setObjectName(_fromUtf8("button_about"))
        self.label = QtGui.QLabel(bzizi)
        self.label.setGeometry(QtCore.QRect(30, 20, 101, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(bzizi)
        self.label_2.setGeometry(QtCore.QRect(30, 140, 101, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(bzizi)
        self.label_3.setGeometry(QtCore.QRect(380, 140, 91, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(bzizi)
        QtCore.QMetaObject.connectSlotsByName(bzizi)

    def retranslateUi(self, bzizi):
        bzizi.setWindowTitle(_translate("bzizi", "正则表达式测试   www.bzizi.com", None))
        self.button_ok.setText(_translate("bzizi", "匹配", None))
        self.button_about.setText(_translate("bzizi", "关于", None))
        self.label.setText(_translate("bzizi", "正则表达式：", None))
        self.label_2.setText(_translate("bzizi", "源文件：", None))
        self.label_3.setText(_translate("bzizi", "匹配字段：", None))

