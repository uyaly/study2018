# !/usr/bin/env python
# -*- coding=gb2312 -*-
# Author:Hiuhung Wan

import random
import time

# 加法
def add_test(sum_value, count):
    '''
    返回指定个数（count）的计算题，以计算某数(sum_value）以内的加法
    :param sum_value: 指定某数以内（的加法）
    :param count: 随机生成多少题
    :return: 返回count个计算题
    '''
    questions = ''
    count_temp = 1   # 计数器

    while True:
        i = random.randrange(1, sum_value)       # 随机生成 第一个加数
        j = random.randrange(2, sum_value + 1)   # 随机生成 和
        l = j - i                                # 第二个加数
        if l > 0:
            str_temp = str(i) + ' + ' + str(l) + '' + ' = \t\t'
            questions += str_temp
            if(count_temp % 5 == 0):
                questions += '\n'
            count_temp += 1
            if count_temp > count:
                break

    return questions
# 减法
def minus_test(sum_value, count):
    '''
    返回指定个数（count）的计算题，以计算某数(sum_value）以内的加法
    :param sum_value: 指定某数以内（的加法）
    :param count: 随机生成多少题
    :return: 返回count个计算题
    '''
    questions = ''
    count_temp = 1   # 计数器

    while True:
        i = random.randrange(1, sum_value)       # 随机生成 第一个数
        j = random.randrange(2, sum_value + 1)   # 随机生成 和
        # l = j - i                                # 第二个加数
        if i > j:
            str_temp = str(i) + ' - ' + str(j) + '' + ' = \t\t'
            questions += str_temp
            if(count_temp % 5 == 0):
                questions += '\n'
            count_temp += 1
            if count_temp > count:
                break

    return questions

def main():
    sum_value, count = 10, 50      # 随机出150题，10以内的加法
    title = '日期：'+ str(time.strftime('%Y-%m-%d',time.localtime(time.time()))) + '   姓名：游文熹    用时：        得分：      \n'
    q = title +  add_test(sum_value, count) + minus_test(sum_value, count)
    str_title = u'%d以内加减算术题%d题.doc'% (sum_value, count+count)
    with open(str_title, "w") as f:
        f.write(q)
    f.close()

if __name__ == '__main__':
    main()