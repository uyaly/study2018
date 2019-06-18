# coding:UTF-8

# pip3 install pypinyin 安装
from PyQt5.QtGui import QIcon
from pypinyin import pinyin, lazy_pinyin
from ui import Ui_MainWindow
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets

class MainUI(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainUI, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("QTableWidget例子")
        # layout=QHBoxLayout()
        self.setWindowIcon(QIcon('logo.png'))
        self.tableWidget=QTableWidget(4,3)
        self.tableWidget.setHorizontalHeaderLabels(['姓名','性别','体重（kg）'])

        self.pushButton.clicked.connect(self.onclick)

    def onclick(self):
        self.outtext = pinyin(self.input.toPlainText(), heteronym=True)
        self.output.setText(self.outtext)


if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # MainWindow = QMainWindow()
    # ui = ui.Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())
    app = QtWidgets.QApplication(sys.argv)
    myui = MainUI()
    myui.show()
    sys.exit(app.exec_())






# for py in py_r:
#     for p in py:
#         print (p,"",)

# py_r = pinyin(u"哥哥", heteronym=True)
# print (py_r)
#
# # 不需要声调
# py_r = lazy_pinyin(u"没有了诗和远方")
# print (py_r)