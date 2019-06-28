# coding:utf-8


import xlrd
from PyQt5.QtWidgets import *
def read_excel(tableWidget3):
    # 打开文件
    workbook = xlrd.open_workbook(u'编码总表.xlsx')
    # workbook = xlrd.open_workbook('/Users/sr00117/Desktop/编码总表.xlsx')
    # 获取所有sheet
    #sheet2_name = workbook.sheet_names()[0]
    # 根据sheet索引或者名称获取sheet内容
    sheet1 = workbook.sheet_by_index(0) # sheet索引从0开始
    cols = sheet1.col_values(1)  # 获取第三列内容 品名
    # print("cols:", cols)
    # 获取整行和整列的值（数组）
    for i in range(1,len(cols)):
        rowslist = sheet1.row_values(i) # 获取excel每行内容
        # print(rowslist)
        for j in range(len(rowslist)):
            #在tablewidget中添加行
            row = tableWidget3.rowCount()
            tableWidget3.insertRow(row)
            #把数据写入tablewidget中
            print(rowslist[j])
            newItem = QTableWidgetItem(rowslist[j])
            tableWidget3.setItem(i-1, j-1, newItem)
