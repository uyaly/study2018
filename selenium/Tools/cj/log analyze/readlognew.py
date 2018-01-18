# coding:utf-8
''''
main function：主要实现把txt中的每行数据写入到excel中
'''
#   第一次执行的代码
import re
import argparse
import sys
import xlwt   # 写入文件
import xlrd     # 打开excel文件

# 新建一个excel文件
file = xlwt.Workbook(encoding='utf-8', style_compression=0)
# 新建一个sheet
sheet = file.add_sheet('data')
# fopen = open(r"D:\PycharmProjects\test\study\lytest\case\cj\3.log", 'r')
fopen = open(r"C:\Users\Administrator\Desktop\teraterm1127.log", 'r')
lines = fopen.readlines()
# 新建一个excel文件
file = xlwt.Workbook(encoding='utf-8', style_compression=0)
# 新建一个sheet
sheet = file.add_sheet('data')

# 写入
i = 0  # 行
j = 0  # 列
for line in lines:
    if line.find('Report') != -1 or line.find('Alarm') != -1:
        p = line.split(' ')
        for j in range(len(p)):
            # print p
            if p[j] != '':
                sheet.write(i, j, p[j])
                j = j+1
            else:
                j = j+1
    i = i+1

file.save(r'C:\Users\Administrator\Desktop\minni.xls')