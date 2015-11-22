#!/usr/bin/python3
# Filename:regex_test.py
#
# Author : haozibi
# Email : b@bzizi.com
# Date:2015-11-19
#
# 不得篡改版权，引用请注明
#

import sys
import re
import string
from PyQt4 import QtCore,QtGui
from regexui import Ui_bzizi

class StartQt4(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_bzizi()
        self.ui.setupUi(self)
        # here we connect signals with our slots
        QtCore.QObject.connect(self.ui.button_ok,QtCore.SIGNAL('clicked()'),self.file_dialog)
       
        QtCore.QObject.connect(self.ui.button_about,QtCore.SIGNAL('clicked()'),self.file_about)

    def file_dialog(self):
        list = []
        list2 = []
        regex = self.ui.text_regex.toPlainText() # 获取正则里内容
        data = self.ui.text_data.toPlainText() # 获取源数据中内容
    
        list = re.compile(regex) # 匹配
        list = re.findall(list,data)
       
        #str = ''.join(list)
        lens = len(list)

        # 利用 list2 把 list 列表中内容进行格式化
        for i in range(0,lens):
            tmp = '[{0}]：{1}\r\n'.format(i,list[i])
            #list2.append(tmp)
            list2 += tmp
        
        
        str = ''.join(list2)
        self.ui.text_show.setText(str)
        print('OK')    
    
    def file_about(self):
        message = QtGui.QMessageBox(self)
        message.setText('联系我:\r\nEmail：b@bzizi.com\r\n网站：www.bzizi.com')
        message.setWindowTitle('About Me !')
        message.setIcon(QtGui.QMessageBox.Question)
        message.exec_()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQt4()
    myapp.show()
    sys.exit(app.exec_())
