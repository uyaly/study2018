import sys
from PyQt5.QtWidgets import *
# from pypinyin import pinyin

from ui import Ui_MainWindow
import xlrd
from PyQt5.QtGui import QIcon
# 列表中的数字显示空白，xls中格式要设置为文本
class Demo(QMainWindow, Ui_MainWindow, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.readExcel(self.tableWidget)
        word = self.InitTable()
        self.pushButton_change.clicked.connect(self.change(word))


    def InitTable(self):
        self.readExcel(self.tableWidget)

    def readExcel(self, tableWidget1):
        data = xlrd.open_workbook(r'data.xls')
        table = data.sheet_by_name('Sheet1')
        # 获取第一行作为key值
        # tableWidget1.setHorizontalHeaderLabels(table.row_values(0))
        # 获取总行数
        rowNum = table.nrows
        # 获取总列数
        colNum = table.ncols
        word = []
        for i in range(rowNum):
            # 从xls取对应每行值
            rowslist = table.row_values(i)
            for j in range(colNum):
                if (j==0)and (i>0):   # 将词组加入队列word
                    word.append(rowslist[j])
                #在tablewidget中添加行
                tableWidget1.setRowCount(rowNum-1)
                tableWidget1.insertRow(rowNum)
                #把数据写入tablewidget中
                newItem = QTableWidgetItem(rowslist[j])
                tableWidget1.setItem(i-1, j, newItem)   # i-1 首行不显示
        return (word)
                # print ("x:",i-1 , "y:", j,"rowslist[j]", rowslist[j])

    # def change(self, word):
    #     py_word = pinyin(word, heteronym=True)   # 开启多音字
    #     print (py_word)

        # 不需要声调
        # py_r = lazy_pinyin(u"没有了诗和远方")
        # print (py_r)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    path = 'logo.png'
    app.setWindowIcon(QIcon(path))  # MAC 下 程序图标是显示在程序坞中的， 切记；
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
