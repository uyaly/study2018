# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(572, 862)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 321, 151))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 51, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.plus = QtWidgets.QLineEdit(self.groupBox)
        self.plus.setGeometry(QtCore.QRect(70, 30, 41, 20))
        self.plus.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.plus.setObjectName("plus")
        self.minus = QtWidgets.QLineEdit(self.groupBox)
        self.minus.setGeometry(QtCore.QRect(70, 60, 41, 20))
        self.minus.setObjectName("minus")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 51, 16))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 90, 51, 16))
        self.label_5.setObjectName("label_5")
        self.plus2 = QtWidgets.QLineEdit(self.groupBox)
        self.plus2.setGeometry(QtCore.QRect(70, 90, 41, 20))
        self.plus2.setObjectName("plus2")
        self.minus2 = QtWidgets.QLineEdit(self.groupBox)
        self.minus2.setGeometry(QtCore.QRect(70, 120, 41, 20))
        self.minus2.setObjectName("minus2")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 120, 51, 16))
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(130, 120, 71, 20))
        self.label_9.setObjectName("label_9")
        self.mix2 = QtWidgets.QLineEdit(self.groupBox)
        self.mix2.setGeometry(QtCore.QRect(210, 120, 41, 20))
        self.mix2.setObjectName("mix2")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(130, 60, 51, 20))
        self.label_11.setObjectName("label_11")
        self.divi = QtWidgets.QLineEdit(self.groupBox)
        self.divi.setGeometry(QtCore.QRect(190, 60, 41, 20))
        self.divi.setObjectName("divi")
        self.mult = QtWidgets.QLineEdit(self.groupBox)
        self.mult.setGeometry(QtCore.QRect(190, 30, 41, 20))
        self.mult.setObjectName("mult")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(130, 30, 51, 20))
        self.label_12.setObjectName("label_12")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(360, 10, 191, 151))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 71, 16))
        self.label_2.setObjectName("label_2")
        self.n_min = QtWidgets.QLineEdit(self.groupBox_2)
        self.n_min.setGeometry(QtCore.QRect(120, 30, 51, 20))
        self.n_min.setObjectName("n_min")
        self.n_sum = QtWidgets.QLineEdit(self.groupBox_2)
        self.n_sum.setGeometry(QtCore.QRect(120, 90, 51, 20))
        self.n_sum.setObjectName("n_sum")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 90, 71, 20))
        self.label_4.setObjectName("label_4")
        self.n_max = QtWidgets.QLineEdit(self.groupBox_2)
        self.n_max.setGeometry(QtCore.QRect(120, 60, 51, 20))
        self.n_max.setObjectName("n_max")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(20, 60, 71, 16))
        self.label_7.setObjectName("label_7")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(20, 120, 71, 20))
        self.label_10.setObjectName("label_10")
        self.n_row = QtWidgets.QLineEdit(self.groupBox_2)
        self.n_row.setGeometry(QtCore.QRect(120, 120, 51, 20))
        self.n_row.setObjectName("n_row")
        self.message_show = QtWidgets.QTextBrowser(self.centralwidget)
        self.message_show.setGeometry(QtCore.QRect(20, 200, 531, 621))
        self.message_show.setObjectName("message_show")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(20, 170, 191, 20))
        self.label_title.setText("")
        self.label_title.setObjectName("label_title")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(210, 170, 161, 20))
        self.label_8.setLineWidth(6)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.report_btn = QtWidgets.QPushButton(self.centralwidget)
        self.report_btn.setGeometry(QtCore.QRect(480, 170, 75, 23))
        self.report_btn.setObjectName("report_btn")
        self.creat_btn = QtWidgets.QPushButton(self.centralwidget)
        self.creat_btn.setGeometry(QtCore.QRect(390, 170, 75, 23))
        self.creat_btn.setObjectName("creat_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 572, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "出题"))
        self.groupBox.setTitle(_translate("MainWindow", "各类题目数量"))
        self.label.setText(_translate("MainWindow", "加法"))
        self.plus.setText(_translate("MainWindow", "0"))
        self.minus.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "减法"))
        self.label_5.setText(_translate("MainWindow", "连加"))
        self.plus2.setText(_translate("MainWindow", "0"))
        self.minus2.setText(_translate("MainWindow", "0"))
        self.label_6.setText(_translate("MainWindow", "连减"))
        self.label_9.setText(_translate("MainWindow", "加减混合"))
        self.mix2.setText(_translate("MainWindow", "0"))
        self.label_11.setText(_translate("MainWindow", "除法"))
        self.divi.setText(_translate("MainWindow", "200"))
        self.mult.setText(_translate("MainWindow", "200"))
        self.label_12.setText(_translate("MainWindow", "乘法"))
        self.groupBox_2.setTitle(_translate("MainWindow", "总配置"))
        self.label_2.setText(_translate("MainWindow", "最小值"))
        self.n_min.setText(_translate("MainWindow", "1"))
        self.n_sum.setText(_translate("MainWindow", "10"))
        self.label_4.setText(_translate("MainWindow", "和最大值"))
        self.n_max.setText(_translate("MainWindow", "10"))
        self.label_7.setText(_translate("MainWindow", "最大值"))
        self.label_10.setText(_translate("MainWindow", "每行几题"))
        self.n_row.setText(_translate("MainWindow", "5"))
        self.report_btn.setText(_translate("MainWindow", "导出"))
        self.creat_btn.setText(_translate("MainWindow", "出题"))

