# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(533, 729)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 100, 491, 581))
        self.tableWidget.setGridStyle(QtCore.Qt.DashLine)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.pushButton_change = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_change.setGeometry(QtCore.QRect(320, 60, 75, 23))
        self.pushButton_change.setObjectName("pushButton_change")
        self.lineEdit_page = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_page.setGeometry(QtCore.QRect(70, 20, 51, 20))
        self.lineEdit_page.setObjectName("lineEdit_page")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 41, 16))
        self.label.setObjectName("label")
        self.pushButton_s_order = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_s_order.setGeometry(QtCore.QRect(420, 20, 75, 23))
        self.pushButton_s_order.setObjectName("pushButton_s_order")
        self.pushButton_s = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_s.setGeometry(QtCore.QRect(320, 20, 75, 23))
        self.pushButton_s.setObjectName("pushButton_s")
        self.lineEdit_word = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_word.setGeometry(QtCore.QRect(180, 20, 51, 20))
        self.lineEdit_word.setText("")
        self.lineEdit_word.setObjectName("lineEdit_word")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 20, 41, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_exam = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exam.setGeometry(QtCore.QRect(420, 60, 75, 23))
        self.pushButton_exam.setObjectName("pushButton_exam")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 533, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "词组"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "拼音"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "页码"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "生词"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Column"))
        self.pushButton_change.setText(_translate("MainWindow", "词组转拼音"))
        self.label.setText(_translate("MainWindow", "页码："))
        self.pushButton_s_order.setText(_translate("MainWindow", "查询错序"))
        self.pushButton_s.setText(_translate("MainWindow", "查询"))
        self.label_2.setText(_translate("MainWindow", "词组："))
        self.pushButton_exam.setText(_translate("MainWindow", "出题"))

