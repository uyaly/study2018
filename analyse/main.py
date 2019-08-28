import datetime
import sys
from PyQt5.QtWidgets import *
from UI import Ui_MainWindow
import analyse
import socket
import threading
flag = False
from PyQt5.QtCore import Qt

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 列表中的数字显示空白，xls中格式要设置为文本
class Demo(QMainWindow, Ui_MainWindow, QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.init_socket()
        self.Button_apart.clicked.connect(self.apart)
        self.Button_join.clicked.connect(self.join)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)   # 0827
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)   # 0827  整行选中
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)   # 0827
        # self.tableWidget.clicked.connect(self.clicklist)
        self.Button_conn.clicked.connect(self.conn)
        self.Button_send.clicked.connect(self.sendmsg)
        self.Button_send.processEvents()

        # self.Button_conn.setCheckable(True)
    def Receve(self,s):
        global flag
        while flag:
            data = s.recv(1024).decode('utf8')
            if data == 'quit':
                flag = False
            # print('recevie news:%s' % data)
            T = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.textEdit_log.insertPlainText('\n' + T + ' RECV :' + '\n')
            self.textEdit_log.insertPlainText(data)

    def conn(self):
        global flag
        global s
        flag = bool(1 - flag)  # flag取反
        hostname = self.lineEdit_IP.text()
        port = int(self.lineEdit_port.text())
        hostport = (hostname, port)
        if flag:
            s.connect(hostport)
            self.Button_conn.setText("断开")
            thrd = threading.Thread(target=self.Receve, args=(s,))
            thrd.start()
        else:
            s.close()
            self.Button_conn.setText("连接")

    def sendmsg(self):
        global flag
        global s
        send_msg = self.textEdit.toPlainText()
        while flag:

            if send_msg == '':
                break
            else:
                s.send(send_msg.encode('utf8'))
                T = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.textEdit_log.insertPlainText('\n' + T + ' SEND :' + '\n')
                self.textEdit_log.insertPlainText(send_msg)
                send_msg = ''
            if send_msg == 'quit':
                flag = False

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
        self.tableWidget.clearContents()
        resultall = analyse.apart(content)
        result = resultall
        # result2 = resultall[1]
        # print(result)
        if isinstance(result,list):
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
        else:
            self.tableWidget.setRowCount(0)
            self.tableWidget.insertRow(0)
            msg = QTableWidgetItem(result)
            self.tableWidget.setItem(0, 1, msg)
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