from PyQt5 import QtWidgets, QtCore
from testqt.TEST_QT_FROM import Ui_Dialog
import sys
from PyQt5.QtCore import *
import time


# 继承QThread
class Runthread(QtCore.QThread):
    # python3,pyqt5与之前的版本有些不一样
    #  通过类成员对象定义信号对象
    _signal = pyqtSignal(str)

    def __init__(self):
        super(Runthread, self).__init__()

    def __del__(self):
        self.wait()

    def run(self):
        print("run 666")
        self._signal.emit("run 666");  # 信号发送


class TestQtFromC(QtWidgets.QWidget, Ui_Dialog):
    text = ""

    def __init__(self):
        super(TestQtFromC, self).__init__()
        self.setupUi(self)

    # click
    def timer_click(self):
        self.thread = Runthread()  # 创建线程
        self.thread._signal.connect(self.callbacklog)  # 连接信号
        self.thread.start()  # 开始线程

    # callback
    def callbacklog(self, msg):
        self.text = self.text + time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime()) + msg + "\n"
        print(self.text)
        # 回调数据输出到文本框
        self.textEdit.setText(self.text);


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mTestQtFromC = TestQtFromC()
    mTestQtFromC.show()
    sys.exit(app.exec_())