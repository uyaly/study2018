# -*- coding:utf-8 -*-
#使用python3.x运行
#需要自己安装slrd包: pip install xlrd
import sys,xlrd,os,importlib
# #python2.x需要添加如下进行编码格式变换
# importlib.reload(sys)
# sys.setdefaultencoding('utf-8')
def xlsInput(data, id_sum):
    for sheet in data.sheets():
        #org_code以sheet子表名为准
        org_code = sheet.name
        #从第二行开始读取（因为从0开始）
        for each in range(1, sheet.nrows):
            #第二列（因为从0开始）
            car = sheet.row_values(each)[1]
            #第三列
            terminal = sheet.row_values(each)[2]
            #第四列
            sim = sheet.row_values(each)[3]
            #判断行数据是否为空
            if '' == car or '' == terminal or '' == sim:
                print(sheet.row_values(each))
                continue
            #生成sql的样式
            strSim = "insert into T_SIMINFO (SIM_ID, ORG_CODE, DEPTCODE, STATE,PAY_MODLE, SIM_NUM) values({}, '{}', '中国移动', 1, '预付费', {});".format(id_sum+each,org_code,sim)

            strTerminal = "insert into T_TERMINALINFO (TERMINAL_ID,TTYPE_ID,SIM_ID,TERMINAL_CODE,ORG_CODE,IS_VIDEO_TERMINAL,SP_SERVER_NAME,PROTOCOL_TYPE,CHANNELS,YT_PROTOCOL_TYPE) " \
                          "values({}, 4, {}, '{}', '{}',1,'1076测试服务器','4',8,'0');".format(id_sum*10+each,id_sum+each,terminal,org_code)

            strCar = "insert into V_VEHICLEINFO (ORG_CODE,VEHICLE_ID,ID_NUMBER,TYPE_ID,TERMINAL_ID,DELETE_FLAG,COLOR_ID_NUMBER_ID,AUTHORIZED_PAY_MASS) " \
                     "values ('{}','{}', '{}', 4, {}, 0, '2',15);".format(org_code, id_sum*100+each, car, id_sum*10+each)
            #写入数据到sql文件中
            with open(org_code + '.sql', 'a') as f:
                f.write(strSim + '\n')
                f.write(strTerminal + '\n')
                f.write(strCar + '\n\n')
        print(org_code+'.sql'+'创建成功！')
        #表数据id编号进行子表连接
        id_sum += sheet.nrows - 1

#查询指定目录下的excel文件，返回一个列表
def xls_file_list():
    xlsFileList = []
    for each in os.listdir('.'):
        if each.split('.')[1] == 'xls' or each.split('.')[1] == 'xlsx':
            xlsFileList.append(each)
    return xlsFileList

#表id编号初始化值
core_id =  20000
#遍历列表中的excel
for each in xls_file_list():
    excelFile = xlrd.open_workbook(each)
    print(each+"表数据识别......")
    #调用函数xlsInput
    xlsInput(excelFile, core_id)
    core_id += 10000
