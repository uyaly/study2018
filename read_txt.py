# coding=utf-8
''''
main function：主要实现把txt中的每行数据写入到excel中
'''
#   第一次执行的代码
import xlwt     #写入文件
import xlrd     #打开excel文件

fopen=open("e:\\a\\bb\\a.txt", 'r')
lines = fopen.readlines()
# 新建一个excel文件
file = xlwt.Workbook(encoding='utf-8', style_compression=0)
# 新建一个sheet
sheet = file.add_sheet('data')

# 写入写入a.txt，a.txt文件有20000行文件
i = 0
for line in lines:
    sheet.write(i, 0, line)
    i = i+1
# 第二层执行代码，写入b.txt，
j = 20001  #从20001行写入
fopen2=open("e:\\a\\bb\\b.txt",'r')
lines2=fopen2.readlines()
for line in lines2:
    sheet.write(j, 0, line)
    j=j+1
file.save('minni.xls')