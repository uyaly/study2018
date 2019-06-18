# -*- coding: utf-8 -*-
# @Author : ratel
# @time : 2019-04-13 18:26
# @file : tg_doorway_add.py
# @software : PyCharm
# 省高警项目 加车
import time
import os
import xlrd


def xls_input(data):
    """
    org_code以sheet子表名为准
    从第二行开始读取（因为从0开始）
    第一列（因为从0开始）
    判断行数据是否为空
    生成sql的样式，创建sql文件并写入
    :param data:
    :return:
    """
    for sheet in data.sheets():
        org_code = sheet.name
        for each in range(1, sheet.nrows):
            ID = sheet.row_values(each)[0]
            PER_ROAD_NO = sheet.row_values(each)[1]
            DOORWAY_NAME = sheet.row_values(each)[2]
            PER_ROAD_NAME = sheet.row_values(each)[3]
            LNG = sheet.row_values(each)[4]
            LAT = sheet.row_values(each)[5]
            TOLL_GATE_ID = sheet.row_values(each)[6]
            TOLL_GATE_NAME = sheet.row_values(each)[7]
            ORG_CODE = sheet.row_values(each)[8]
            ORG_NAME = sheet.row_values(each)[9]
            IN_OUT_TYPE = sheet.row_values(each)[10]
            DIR_NO = sheet.row_values(each)[11]

            if '' == ID or '' == PER_ROAD_NO or '' == DOORWAY_NAME or '' == PER_ROAD_NAME or '' == LNG or \
                    '' == LAT or '' == TOLL_GATE_ID or TOLL_GATE_NAME == '' or ORG_CODE == '' or \
                    ORG_NAME == '' or IN_OUT_TYPE == '' or DIR_NO == '':
                print(sheet.row_values(each))
                continue
            strDoorway = "insert into IOTC5WEB.BH_PBDM_TG_DOORWAY(ID,PER_ROAD_NO,DOORWAY_NAME,PER_ROAD_NAME,LNG,LAT," \
                         "TOLL_GATE_ID,TOLL_GATE_NAME,ORG_CODE,org_name,IN_OUT_TYPE,DIR_NO) values('{}','{}','{}'," \
                         "'{}','{}','{}','{}','{}','{}','{}','{}','{}');".format(ID, PER_ROAD_NO, DOORWAY_NAME,
                         PER_ROAD_NAME, LNG, LAT, TOLL_GATE_ID, TOLL_GATE_NAME, ORG_CODE, ORG_NAME, IN_OUT_TYPE, DIR_NO)

            with open(org_code + time.strftime("%Y%m%d%H%M%S", time.localtime()) + '.sql', 'a') as f:
                f.write(strDoorway + '\n')

        print('创建成功！')


def xls_file_list():
    """
    查询指定目录下的excel文件，返回一个列表
    :return:
    """
    xlsFileList = []
    for each in os.listdir('.'):
        if each.split('.')[1] == 'xls' or each.split('.')[1] == 'xlsx':
            xlsFileList.append(each)
    return xlsFileList


def output_sql(table_name):
    """
    遍历列表中的excel,当获取到指定表时，生成sql
    :param table_name:
    :return:
    """
    for each in xls_file_list():

        if each == table_name:
            excel_file = xlrd.open_workbook(each)
            print(excel_file)
            print(each+"表数据识别......")
            # 调用函数xlsInput
            xls_input(excel_file)


if __name__ == '__main__':
    output_sql("BH_PBDM_TG_DOORWAY.xls")