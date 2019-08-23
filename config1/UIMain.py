# !/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

from PyQt5.QtWidgets import *
from UI import Ui_MainWindow
import main

class Demo(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(Demo, self).__init__()
        self.setupUi(self)
        self.initCreate()


    def initCreate(self):
        # if self.textEdit.toPlainText() is not '':
        self.textEdit.textChanged.connect(self.Analysis)


    def Analyz(self):
        content = self.textEdit.toPlainText()
        result = main.json_txt(content)
        self.label.setText(result)

        # self.label.setText("00000000000c000201ab7d6706e23f5b001b00000000190613122316010400005daa02020000030200002504000000002a0200022b0400010000300113310113")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    d = Demo()
    d.show()
    sys.exit(app.exec_())

