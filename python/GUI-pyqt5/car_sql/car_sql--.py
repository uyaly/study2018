# -*- coding:utf-8 -*-
#使用python3.x运行
#需要自己安装slrd包: pip install xlrd
import sys,xlrd,os,importlib
# #python2.x需要添加如下进行编码格式变换
# importlib.reload(sys)
# sys.setdefaultencoding('utf-8')
from math import ceil

totle = 10000         # 多少辆车
carcount = 10000       # 每个部门多少车
orgnum = 2501           # 部门编号尾号初始值 ：部门编号B000
carnum = 00000          # 车牌：测B
terminalnum = 0000000000   # 设备编号初始值
simnum = 13100000000    # SIM卡号初始值
IMEInum  = 123456789120000  # IMEI初始值
TTYPE_ID = 57   # 终端类型2019检测在数据库中的编号
def xlsInput(totle, id_sum):   # totle1每次循环次数
    org_code = 'B000' + str(orgnum)   # 部门编号B0000801
    # id_sum = 10          # 多少辆车
    global carnum
    global terminalnum
    global simnum
    global IMEInum
    global TTYPE_ID
    for each in range(0, totle):
        # 终端编号ID
        terminal = 'AAAAAAAAAABBBBBBBBBB' + str("{0:>010s}".format(str(terminalnum)))
        terminalnum += 1
        #车牌号
        car = u'测B'+ str("{0:>05s}".format(str(carnum))) # 不足5位补0
        carnum += 1

        # sim卡号
        sim = str(simnum)
        simnum += 1
        # IMEI
        IMEI = str(IMEInum)
        IMEInum += 1

        #生成sql的样式
        strSim = "insert into T_SIMINFO (SIM_ID, ORG_CODE, DEPTCODE, STATE,PAY_MODLE, SIM_NUM,IMEI) values({}, '{}', '中国移动', 1, '预付费', {},{});".format(id_sum+each+1,org_code,sim,IMEI)

        strTerminal = "insert into T_TERMINALINFO (TERMINAL_ID,TTYPE_ID,SIM_ID,TERMINAL_CODE,ORG_CODE,IS_VIDEO_TERMINAL,SP_SERVER_NAME,PROTOCOL_TYPE,CHANNELS,YT_PROTOCOL_TYPE) " \
                      "values({}, {}, {}, '{}', '{}',1,'1076测试服务器','4',8,'0');".format(id_sum*10+each+1,TTYPE_ID,id_sum+each+1,terminal,org_code)

        strCar = "insert into V_VEHICLEINFO (ORG_CODE,VEHICLE_ID,ID_NUMBER,TYPE_ID,TERMINAL_ID,DELETE_FLAG,COLOR_ID_NUMBER_ID,AUTHORIZED_PAY_MASS) " \
                 "values ('{}','{}', '{}', 4, {}, 0, '2',15);".format(org_code, id_sum*100+each+1, car, id_sum*10+each+1)
        #写入数据到sql文件中
        with open(org_code + '.sql', 'a') as f:
            f.write(strSim + '\n')
            f.write(strTerminal + '\n')
            f.write(strCar + '\n\n')
    print(org_code+'.sql'+'创建成功！')

orgall = ceil(totle/carcount)  # 部门个数

# 表id编号初始化值
core_id =  70000
# 每个部门循环carcount笔
for each in range(0, orgall):
    # print (each)
    #调用函数xlsInput
    if totle <= carcount:
        xlsInput(totle, core_id)
    elif totle > carcount:
        xlsInput(carcount, core_id)
        totle -= carcount
    core_id += carcount
    orgnum += 1