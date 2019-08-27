import os
import sys
import threading
import time
from PyQt5.QtWidgets import *
from UI import Ui_MainWindow
import analyse
import socket

# 列表中的数字显示空白，xls中格式要设置为文本
class Demo(QMainWindow, Ui_MainWindow, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.init_create()
        self.Button_apart.clicked.connect(self.apart)
        self.Button_join.clicked.connect(self.join)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)   # 0827
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)   # 0827  整行选中
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)   # 0827
        # self.tableWidget.clicked.connect(self.clicklist)
        self.Button_conn.clicked.connect(self.conn)
        self.flag = False
    #
    # def clicklist(self):
    #     items = self.tableWidget.selectRow()
        # self.tableWidget.row(items.at(i))

    def conn(self):
        hostname = self.lineEdit_IP.text()
        port = self.lineEdit_port.text()
        if '' == hostname or '' == port:
            print('请输入ip与端口')
        else:
            addr = (hostname, int(port))
            clientsock = socket.socket()
            clientsock.connect(addr)
            self.Button_send.clicked.connect(self.sendmsg(clientsock))
            while True:
                send_msg = self.textEdit.toPlainText()
                if not send_msg:
                    break
                self.textEdit_log.insertPlainText(self.textEdit.toPlainText())
                clientsock.send(bytes(send_msg, encoding='gbk'))
                recvdata = clientsock.recv(1024)
                if not recvdata:
                    break
                print(recvdata)
        clientsock.close()

    def sendmsg(self, clientsock):
        flag = True
        while True:
            send_msg = self.textEdit.toPlainText()

            if not send_msg:
                break
            self.textEdit_log.insertPlainText(self.textEdit.toPlainText())
            clientsock.send(bytes(data, encoding='gbk'))
            recvdata = clientsock.recv(1024)
            if not recvdata:
                break
            print(recvdata)

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
            key.setFlags(Qt.ItemIsEnabled)      # 0827
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