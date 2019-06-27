# -*- coding: utf-8 -*-
# @Author : ratel
# @time : 2019-04-01 11:14
# @file : run.py
# @software : PyCharm

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
from hits import Ui_MainWindow
from PlatformManagement import add_user, reset_password
# import UserThread
import sys


class MainUI(QtWidgets.QMainWindow, Ui_MainWindow):
    """
    执法类，继承QMainWindow与生成类Ui_MainWindow
    """

    def __init__(self, parent=None):
        super(MainUI, self).__init__(parent)
        self.setupUi(self)

        self.setWindowIcon(QIcon('logo.png'))
        # 平台管理->添加用户
        # 设置个数缺省为不可输入
        self.add_user_sum_lineEdit.setEnabled(False)
        # 用户新增槽函数，点击确认时触发
        self.add_user_pushButton.clicked.connect(self.add_user)
        # 用户新增重置槽函数，点击重置时触发
        self.add_user_reset_pushButton.clicked.connect(self.add_user_reset)
        # 平台管理->用户管理->重置密码
        self.user_passswd_reset_pushButton.clicked.connect(self.reset_password)

    @QtCore.pyqtSlot(int)
    def on_add_user_type_comboBox_activated(self, index):
        """
        装饰器自定义槽函数命令规则：on + 使用setObjectName设置的名称 + 信号名称
        1、获取用户下拉框选择的index
        2.txt、判断index，如果为1 （批量添加），则个数输入框置为可输入，否则个数输入框为不可输入
        :return:
        """
        index = self.add_user_type_comboBox.currentIndex()
        if index == 1:
            self.add_user_sum_lineEdit.setEnabled(True)
        else:
            self.add_user_sum_lineEdit.setEnabled(False)

    def closeEvent(self, event):
        """
        重写关闭函数
        :param event:
        :return:
        """
        reply = QtWidgets.QMessageBox.question(self, '关闭程序', '确定要关闭并退出程序吗？',
                                               QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def add_user_reset(self):
        """
        用户新增->重置
        :return:
        """
        self.add_user_username_lineEdit.clear()
        # 重置下拉框为第一个选项
        self.add_user_type_comboBox.setCurrentIndex(0)
        self.add_user_sum_lineEdit.clear()

    def add_user(self):
        """
        用户新增
        1、获取用户输入：self.add_user_username_lineEdit.text()
        2.txt、判断account 是否为null，是则提示，不是进行下步判断
        3、下一步判断sum(个数)是否为null,是则为单个添加，调用add_user添加后输入日志到log_textBrowser中
            否，则进行下一步判断
        4、下一步判断sum是否为整数，是，则多线程创建，否，则提示非法输入
        :return:
        """
        account = self.add_user_username_lineEdit.text()
        sum = self.add_user_sum_lineEdit.text()
        print(sum)
        if account == '':
            self.log_textBrowser.append("请输入：用户名!!!")
        else:
            if sum == '':
                add_user_resp = add_user(account)
                self.log_textBrowser.append(str(add_user_resp))
            elif sum.isdigit():
                # 线程启动锁定 确认 按钮
                self.add_user_pushButton.setDisabled(True)
                # 创建线程
                self.add_user_thread = UserThread(account, sum)
                # 将信号连接到槽函数add_user_append，输出日志
                self.add_user_thread.log_textBrowser.connect(self.add_user_append)
                # 将信号连接到槽函数add_user_pushon，打开 确认 按钮锁
                self.add_user_thread.finished.connect(self.add_user_pushon)
                # 线程启动
                self.add_user_thread.start()
                pass
            else:
                self.log_textBrowser.append("个数输入非法！！！")

    def add_user_append(self, astr):
        """
        将日志添加到log_textBrowser中
        :param astr:
        :return:
        """
        self.log_textBrowser.append(astr)

    def add_user_pushon(self):
        """
        把 确认 按钮 锁定状态解除
        :return:
        """
        self.add_user_pushButton.setDisabled(False)

    def reset_password(self):
        """
        用户密码重置
        1、获取用户输入用户名account
        2.txt、调用密码重置函数reset_password
        3、把返回结果显示在log_textBrowser中
        :return:
        """
        account = self.user_passwd_username_lineEdit.text()
        if account == '':
            self.log_textBrowser.append("请输入：用户名!!!")
        else:
            reset_password_resp = reset_password(account)
            self.log_textBrowser.append(str(reset_password_resp))


class UserThread(QtCore.QThread):
    """
    用户新增线程
    1、创建一个信号
    2.txt、初始化用户输入数据
    3、重置run函数
    """
    log_textBrowser = QtCore.pyqtSignal(str)

    def __init__(self, account, sum):
        super(UserThread, self).__init__()
        self.account = account
        self.sum = sum

    def run(self):
        # 空一行
        self.log_textBrowser.emit("")
        # 循环执行添加操作
        for i in range(int(self.sum)):
            # 用户名 = 用户名 + i
            account = self.account + str(i)
            add_user_resp = add_user(account)
            add_log = str(i + 1) + '--添加用户--' + account + str(add_user_resp)
            # 格式化输入日志到log_textBrowser
            self.log_textBrowser.emit(str(add_log))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myui = MainUI()
    myui.show()
    sys.exit(app.exec_())