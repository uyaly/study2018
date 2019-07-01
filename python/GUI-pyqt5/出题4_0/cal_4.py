# !/usr/bin/env python
# -*- coding:utf-8 -*-
import random
from itertools import product
import sys

import time

from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import *
from UI import Ui_MainWindow

class Demo(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(Demo, self).__init__()
        self.setupUi(self)
        self.initCreate()


    def initCreate(self):
        settings = QSettings("config.ini", QSettings.IniFormat)
        #settings = QSettings("mysoft","myapp")                        #方法2：使用注册表
        self.plus.setText(settings.value("plus_count"))
        self.minus.setText(settings.value("minus_count"))
        self.plus2.setText(settings.value("plus2_count"))
        self.minus2.setText(settings.value("minus2_count"))
        self.mix2.setText(settings.value("mix2_count"))
        self.n_min.setText(settings.value("n_min"))
        self.n_max.setText(settings.value("n_max"))
        self.n_sum.setText(settings.value("n_sum"))
        self.n_row.setText(settings.value("n_row"))

        self.creat_btn.clicked.connect(self.mix)
        self.report_btn.clicked.connect(self.exportword)


    #  # 保存信息
    def save_login_info(self):
        settings = QSettings("config.ini", QSettings.IniFormat)        #方法1：使用配置文件
        #settings = QSettings("mysoft","myapp")                        #方法2：使用注册表
        settings.setValue("plus_count",self.plus.text())        #  加法题数量
        settings.setValue("minus_count", self.minus.text())     #  减法题数量
        settings.setValue("plus2_count", self.plus2.text())     #  连加题数量
        settings.setValue("minus2_count", self.minus2.text())   #  连减题数量
        settings.setValue("mix2_count", self.mix2.text())   #  混合题数量
        settings.setValue("n_min", self.n_min.text())   #  最小值
        settings.setValue("n_max", self.n_max.text())   #  最大值
        settings.setValue("n_sum", self.n_sum.text())   #  最大和
        settings.setValue("n_row", self.n_row.text())   #  每行多少题

    def base_plus(self, n_min, n_max, n_sum):
        plus_all = []
        # 两位运算的不重复个数
        for x,y in product(range(n_min,n_max+1), repeat=2):
            if (x + y <= n_sum):
                plus = str(x).rjust(2) + ' +' + str(y).rjust(2) + ' =     '      #  按2位数右对齐
                plus_all.append(plus)
        # print ("加法"+str(len(plus_all)))
        return plus_all

    def base_minus(self, n_min, n_max, n_sum):
        minus_all = []
        # 两位运算的不重复个数
        for x,y in product(range(n_min,n_max+1), repeat=2):
            if (x - y >= 0):
                minus = str(x).rjust(2) + ' -' + str(y).rjust(2) + ' =     '     #  按2位数右对齐
                minus_all.append(minus)
        # print ("减法"+str(len(minus_all)))
        return minus_all

    def base_plus2(self, n_min, n_max, n_sum):
        plus2_all = []
        # 三位运算的不重复个数
        for x,y,z in product(range(n_min, n_max+1), repeat=3):
            if (x + y + z <= n_sum):
                plus2 = str(x).rjust(2) + ' +' + str(y).rjust(2) + ' +' + str(z).rjust(2) + ' =     '      #  按2位数右对齐
                plus2_all.append(plus2)
        # print ("连加"+str(len(plus2_all)))
        return plus2_all

    def base_minus2(self, n_min, n_max, n_sum):
        minus2_all = []
        # 三位运算的不重复个数
        for x,y,z in product(range(n_min, n_max+1), repeat=3):
            if (x - y - z >= 0):
                minus2 = str(x).rjust(2) + ' -' + str(y).rjust(2) + ' -' + str(z).rjust(2) + ' =     '     #  按2位数右对齐
                minus2_all.append(minus2)
        # print ("连减"+str(len(minus2_all)))
        return minus2_all

    def base_mix2(self, n_min, n_max, n_sum):
        mix2_all = []
        # 三位运算的不重复个数
        for x,y,z in product(range(n_min, n_max+1), repeat=3):
            if (x + y - z >= 0)and(x + y - z <= n_sum):
                mix1 = str(x).rjust(2) + ' +' + str(y).rjust(2) + ' -' + str(z).rjust(2) + ' =     '     #  按2位数右对齐
                mix2_all.append(mix1)
            if (x - y + z >= 0)and((x - y + z <= n_sum)):
                mix2 = str(x).rjust(2) + ' -' + str(y).rjust(2) + ' +' + str(z).rjust(2) + ' =     '     #  按2位数右对齐
                mix2_all.append(mix2)
        # print ("-++-"+str(len(mix2_all)))
        return mix2_all

    def mix(self):
        self.message_show.clear()
        resultList = []
        #  加法题数量
        if self.plus.text() == '':
            plus_count = 0
        else:
            plus_count = int(self.plus.text())
        #  减法题数量
        if self.minus.text() == '':
            minus_count = 0
        else:
            minus_count = int(self.minus.text())
        #  连加题数量
        if self.plus2.text() == '':
            plus2_count = 0
        else:
            plus2_count = int(self.plus2.text())
        #  连减题数量
        if self.minus2.text() == '':
            minus2_count = 0
        else:
            minus2_count = int(self.minus2.text())
        #  混合题数量
        if self.mix2.text() == '':
            mix2_count = 0
        else:
            mix2_count = int(self.mix2.text())

        n_min = int(self.n_min.text())
        n_max = int(self.n_max.text())
        n_sum = int(self.n_sum.text())
        n_row = int(self.n_row.text())
        count = 0

        if (plus_count > 0):  # 有加法 45不重
            count += plus_count
            result = self.base_plus(n_min, n_max, n_sum)
            if plus_count > len(result):
                resultList += result
                for k in range(plus_count-len(result)):
                    resultList.append(random.choice(result))
            else:
                resultList += random.sample(result, plus_count)


        if (minus_count > 0):  # 有减法 55不重
            count += minus_count
            result  = self.base_minus(n_min, n_max, n_sum)
            if minus_count > len(result):
                resultList += result
                for k in range(minus_count-len(result)):
                    resultList.append(random.choice(result))
            else:
                resultList += random.sample(result, minus_count)

        if (plus2_count > 0):  # 连加法 120不重
            count += plus2_count
            result  = self.base_plus2(n_min, n_max, n_sum)
            if plus2_count > len(result):
                resultList += result
                for k in range(plus2_count-len(result)):
                    resultList.append(random.choice(result))
            else:
                resultList += random.sample(result, plus2_count)

        if (minus2_count > 0):  # 连减法 165不重
            count += minus2_count
            result  = self.base_minus2(n_min, n_max, n_sum)
            if minus2_count > len(result):
                resultList += result
                for k in range(minus2_count-len(result)):
                    resultList.append(random.choice(result))
            else:
                resultList += random.sample(result, minus2_count)

        if (mix2_count > 0):  # 混合加减法  1430不重（715*2.txt）
            count += mix2_count
            result  = self.base_mix2(n_min, n_max, n_sum)
            if mix2_count > len(result):
                resultList += result
                for k in range(mix2_count-len(result)):
                    resultList.append(random.choice(result))
            else:
                resultList += random.sample(result, mix2_count)

        random.shuffle(resultList)
        for k in range(len(resultList)):
            self.message_show.insertPlainText(resultList[k])
            if (k+1)%n_row == 0:
                self.message_show.append('\n')

        self.label_title.setText(u'{0}以内{1}道'.format(n_max, count))
        self.label_8.setText('重复个数为：{0}'.format(count-len(set(resultList))))
        self.save_login_info()

    def exportword(self):
        str_title = self.label_title.text() + str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))) + '.doc'
        title = self.label_title.text() + '\n' + u'日期：'+ str(time.strftime('%Y-%m-%d',time.localtime(time.time()))) + u'   姓名：        用时：        得分：      \n'
        q = (title + self.message_show.toPlainText())
        with open(str_title, "w") as f:
            f.write(q)
        f.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    d = Demo()
    d.show()
    sys.exit(app.exec_())

