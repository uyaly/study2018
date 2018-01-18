# coding:utf-8
''''
main function：主要实现把txt中的每行数据写入到excel中
'''
#   第一次执行的代码

import xlwt   # 写入文件
import xlrd     # 打开excel文件
fopen = open(r"D:\3.log", 'r')
lines = fopen.readlines()
# 新建一个excel文件
file = xlwt.Workbook(encoding='utf-8', style_compression=0)
# 新建一个sheet
sheet = file.add_sheet('data')

# 写入
i = 0
for line in lines:
    sheet.write(i, 0, line)
    i = i+1

file.save(r'C:\Users\Administrator\Desktop\minni.xls')