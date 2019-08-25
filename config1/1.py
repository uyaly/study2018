import sys
from PyQt5.QtWidgets import *
from UI import Ui_MainWindow
import main1
from PyQt5.QtGui import QIcon
# 列表中的数字显示空白，xls中格式要设置为文本
class Demo(QMainWindow, Ui_MainWindow, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_create()
        # self.pushButton_change.clicked.connect(self.change(word))

    def init_create(self):
        self.Button_analyz.clicked.connect(self.analyse)
        # self.Button_create.clicked.connect(self.create)


    def create(self):
        # context =
        self.textEdit.clear()
        # self.textEdit.setText(context)



    def analyse(self):
        content = self.textEdit.toPlainText()
        resultall = main1.json_txt(content)
        result = resultall[0]
        result2 = resultall[1]
        print(result2)
        for i in range(len(result)):
            #在tablewidget中添加行
            self.tableWidget.setRowCount(len(result)-1)
            self.tableWidget.insertRow(len(result)-1)
            #把数据写入tablewidget中
            key = QTableWidgetItem(result[i][0])
            value = QTableWidgetItem(result[i][1])
            self.tableWidget.setItem(i, 0, key)   # i-1 首行不显示
            self.tableWidget.setItem(i, 1, value)   # i-1 首行不显示

        for j in range(len(result2)):
            # print(result2[j])
            #在tablewidget1中添加行
            self.tableWidget_2.setRowCount(len(result2)-1)
            self.tableWidget_2.insertRow(len(result2)-1)
            #把数据写入tablewidget1中
            key1 = QTableWidgetItem(result2[j][0])
            value1 = QTableWidgetItem(result2[j][1])
            self.tableWidget_2.setItem(j, 0, key1)   # i-1 首行不显示
            self.tableWidget_2.setItem(j, 1, value1)   # i-1 首行不显示

if __name__ == '__main__':
    app = QApplication(sys.argv)
    path = 'logo.png'
    app.setWindowIcon(QIcon(path))  # MAC 下 程序图标是显示在程序坞中的， 切记；
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())