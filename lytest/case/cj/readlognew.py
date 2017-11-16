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


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file')
    args = parser.parse_args()

    # if not args.file:
    #     print 'Usage: python analyze_log -f <log_file>'
    #     sys.exit(-1)

    re_fum = re.compile('(?<= )[A-F0-9]{2}')

    with open(r"D:\3.log", 'r') as f:
        line = f.readline()
        while line:
            if not line.startswith('Report'):
                line = f.readline()
                continue
            # get new line
            # sheet.write(0, 0, "type")
            # sheet.write(0, 1, "time")
            # sheet.write(0, 2, "sta")
            # sheet.write(0, 3, "alarm")
            i = 1
            for i in range(len(line)):
                try:
                    args = line.split(' ')
                    type = args[0]
                    time = args[1]
                    num = args[2]
                    extra = args[4]

                    if j:
                        sheet.write(i, j, args[j])
                        j = j+1
                except:
                    continue

                send_bufs = []
                recv_bufs = []
                send_buf = []
                recv_buf = []
                is_sending = True
                while True:
                    line = f.readline()
                    values = re_fum.findall(line)
                    if not values:
                        if send_buf and recv_buf:
                            send_bufs.append(send_buf)
                            recv_bufs.append(recv_buf)
                        print '''Type: {}\nTime: {}\nNumber: {}\nExtra: {}'''.format(type, time, num, extra)

                        for i in xrange(len(send_bufs)):
                            print 'Send: {}'.format(' '.join(send_bufs[i]))
                            print 'Recv: {}'.format(' '.join(recv_bufs[i]))
                        break
                    else:
                        if values[0] == '7E':
                            is_sending = True
                            if send_buf and recv_buf:
                                send_bufs.append(send_buf)
                                recv_bufs.append(recv_buf)
                            send_buf = []
                            recv_buf = []
                        if is_sending:
                            send_buf.extend(values)
                        else:
                            recv_buf.extend(values)
                        if values[-1] == '7E':
                            is_sending = False

# fopen = open(r"D:\3.log", 'r')
# lines = fopen.readlines()
# 新建一个excel文件
# file = xlwt.Workbook(encoding='utf-8', style_compression=0)
# 新建一个sheet
# sheet = file.add_sheet('data')

# 写入
# i = 0  # 行
# j = 0  # 列
# for line in lines:
    # if line.find('Report') != -1 or line.find('Alarm') != -1:
    #     p = line.split(' ')
    #     for j in range(len(p)):
    #         # print p
    #         if p[j] != '':
    #             sheet.write(i, j, p[j])
    #             j = j+1
    #         else:
    #             j = j+1
    # i = i+1

file.save(r'C:\Users\Administrator\Desktop\minni.xls')