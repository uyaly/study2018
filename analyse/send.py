import os
import sys
import threading
# from old import send_thread
from PyQt5.QtWidgets import *
from UI import Ui_MainWindow
import analyse


# 列表中的数字显示空白，xls中格式要设置为文本
class Demo(QMainWindow, Ui_MainWindow, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.init_create()
        self.Button_apart.clicked.connect(self.apart)
        self.Button_join.clicked.connect(self.join)
        self.flag = False

    # def init_create(self):
    #     self.Button_apart.clicked.connect(self.apart)
    #     self.Button_join.clicked.connect(self.join)
        # self.Button_conn.clicked.connect(self.conn)
        # self.Button_disconn.clicked.connect(self.disconn)

    # def conn(self):
    #     ip = self.lineEdit_IP.text()
    #     port = self.lineEdit_port.text()
    #     if '' == ip or '' == port:
    #         print('请输入ip与端口')
        # 点击开始按钮
        # elif self.flag == False:
        #     self.flag = True
        #     # self.Button_join.
        #     # ().config(relief=SUNKEN, text='断开')
        #     thread = threading.Thread(target=self.Count)
        #     thread.setDaemon(True)
        #     thread.start()
        #
        #     t = threading.Thread(target=self.threadStart,
        #                          args=(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\car', ip, port))
        #     t.setDaemon(True)
        #     t.start()
        # # 点击结束按钮
        # else:
        #     self.flag = False
        #
        #     # self.bStart.config(relief=RAISED, text="连接")
        #     self.threadStop()

    # def threadStart(self, fileDir, ip, port):
    #     print(os.getcwd())
    #     fileList = os.listdir(fileDir)
    #     filePath = os.getcwd() + '\\' + fileDir
    #
    #     self.stopList = []
    #     for each in fileList:
    #         runGPS = send_thread.ThreadGPS((filePath + '\\' + each), ip, int(port))
    #         self.stopList.append(runGPS)
    #         tGPS = threading.Thread(target=runGPS.run)
    #         tGPS.setDaemon(True)
    #         tGPS.start()
    #         time.sleep(20)

    # def threadStop(self):
    #     for each in self.stopList:
    #         each.stop()

    def join(self):
        list = []
        # columnCount  =self.tableWidget.columnCount()
        rowCount = self.tableWidget.rowCount()
        for i in range(rowCount):
            list.append(self.tableWidget.item(i,1).text())
            # print(list[i]+'\n')
        # print(list)
        context = analyse.join(list)
        self.textEdit.clear()
        self.textEdit.setText(context)

    def apart(self):
        content = self.textEdit.toPlainText()
        resultall = analyse.apart(content)
        result = resultall
        # result2 = resultall[1]
        # print(result)
        for i in range(len(result)):
            #在tablewidget中添加行
            self.tableWidget.setRowCount(len(result)-1)
            self.tableWidget.insertRow(len(result)-1)
            #把数据写入tablewidget中
            key = QTableWidgetItem(result[i][0])
            value = QTableWidgetItem(result[i][1])
            self.tableWidget.setItem(i, 0, key)   # i-1 首行不显示
            self.tableWidget.setItem(i, 1, value)   # i-1 首行不显示

        # for j in range(len(result2)):
        #     # print(result2[j])
        #     #在tablewidget1中添加行
        #     self.tableWidget_2.setRowCount(len(result2)-1)
        #     self.tableWidget_2.insertRow(len(result2)-1)
        #     #把数据写入tablewidget1中
        #     key1 = QTableWidgetItem(result2[j][0])
        #     value1 = QTableWidgetItem(result2[j][1])
        #     self.tableWidget_2.setItem(j, 0, key1)   # i-1 首行不显示
        #     self.tableWidget_2.setItem(j, 1, value1)   # i-1 首行不显示

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())