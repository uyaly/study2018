# -*- coding:utf-8 -*-
# 使用python3.x运行
# 需要UI.py
# #python2.x需要添加如下进行编码格式变换
# importlib.reload(sys)
# sys.setdefaultencoding('utf-8')
import glob

from math import ceil
from PyQt5.QtWidgets import *
import sys
import os

from UI import Ui_MainWindow

class Demo(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(Demo, self).__init__()
        self.setupUi(self)
        self.initConnect()

    def initConnect(self):
        self.creatsql_btn.clicked.connect(self.creatsql)

    def creatsql(self):
        global orgnum
        global carnum
        global terminalnum
        global simnum
        totle = int(self.car_totle.text())
        orgnum = int(self.org_num.text())
        carcount = int(self.org_carcount.text())
        carnum = int(self.car_carnum.text())
        terminalnum = int(self.car_terminalnum.text())
        simnum = int(self.car_simnum.text())
        orgall = ceil(totle/carcount)  # 部门个数

        self.deletesql()   # 删除已生成的*.sql文件

        self.message_show.clear()   # 清空日志信息
        # 表id编号初始化值
        core_id =  20000
        # 每个部门循环carcount笔
        for each in range(0, orgall):
            # print (each)
            #调用函数xlsInput
            if totle <= carcount:
                msg = self.xlsInput(totle, core_id)
            elif totle > carcount:
                msg = self.xlsInput(carcount, core_id)
                totle -= carcount
            core_id += carcount
            orgnum += 1
            self.message_show.append(msg)
            QApplication.processEvents()  # 界面实时刷新

    def deletesql(self):
        for infile in glob.glob(os.path.join('*.sql')):
            os.remove(infile)

    def xlsInput(self, totle, id_sum):   # totle每次循环次数

        org_code = 'B1000' + str(orgnum)   # 部门编号B0000801
        global carnum
        global terminalnum
        global simnum
        for each in range(0, totle):
            #车牌号
            car = u'测B'+ str(carnum)
            carnum += 1
            # 终端编号
            terminal = str(terminalnum)
            terminalnum += 1
            # sim卡号
            sim = str(simnum)
            simnum += 1

            #生成sql的样式
            strSim = "insert into T_SIMINFO (SIM_ID, ORG_CODE, DEPTCODE, STATE,PAY_MODLE, SIM_NUM) values({}, '{}', '中国移动', 1, '预付费', {});".format(id_sum+each+1,org_code,sim)

            strTerminal = "insert into T_TERMINALINFO (TERMINAL_ID,TTYPE_ID,SIM_ID,TERMINAL_CODE,ORG_CODE,IS_VIDEO_TERMINAL,SP_SERVER_NAME,PROTOCOL_TYPE,CHANNELS,YT_PROTOCOL_TYPE) " \
                          "values({}, 4, {}, '{}', '{}',1,'1076测试服务器','4',8,'0');".format(id_sum*10+each+1,id_sum+each+1,terminal,org_code)

            strCar = "insert into V_VEHICLEINFO (ORG_CODE,VEHICLE_ID,ID_NUMBER,TYPE_ID,TERMINAL_ID,DELETE_FLAG,COLOR_ID_NUMBER_ID,AUTHORIZED_PAY_MASS) " \
                     "values ('{}','{}', '{}', 4, {}, 0, '2.txt',15);".format(org_code, id_sum*100+each+1, car, id_sum*10+each+1)
            #写入数据到sql文件中
            with open(org_code + '.sql', 'a') as f:
                f.write(strSim + '\n')
                f.write(strTerminal + '\n')
                f.write(strCar + '\n\n')
        return (org_code+'.sql'+'创建成功！')
        # print (org_code+'.sql'+'创建成功！')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    d = Demo()
    d.show()
    sys.exit(app.exec_())
