# coding:utf-8
''''
main function：主要实现把txt中的每行数据写入到excel中
'''
#   第一次执行的代码
import re
import xlwt   # 写入文件
import xlrd     # 打开excel文件
fopen = open(r"D:\3.log", 'r')
lines = fopen.readlines()

# 新建一个excel文件
file = xlwt.Workbook(encoding='utf-8', style_compression=0)
# 新建一个sheet
sheet = file.add_sheet('data')

# 写入xls
i = 0
j = 0
for line in lines:
    # print line
    # 判断开头是Report或者alarm的，在空格处分列显示
    if line.find("Report") != -1 or line.find("Alarm") != -1:
        p = line.split(' ')
        # print p
        for j in range(len(p)):
            # 对空数据处理
            if p[j] == '':
                j = j+1
            else:
                sheet.write(i, j, p[j])
                j = j+1

    if line.find("1000") != -1:
        print re.search('([0-9A-F][0-9A-F] |){2}', line, flags=0)

    else:
        pass
    i = i+1

file.save(r'C:\Users\Administrator\Desktop\minni.xls')