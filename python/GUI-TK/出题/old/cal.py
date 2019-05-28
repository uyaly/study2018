# !/usr/bin/env python
# -*- coding=gb2312 -*-

import random
import time

# 加法
def add1(sum_value, count):
    '''
    返回指定个数（count）的计算题，以计算某数(sum_value）以内的加法
    :param sum_value: 指定某数以内（的加法）
    :param count: 随机生成多少题
    :return: 返回count个计算题
    '''
    questions = ''
    count_temp = 1   # 计数器

    while True:
        i = random.randint(1, int(sum_value))       # 随机生成 第一个加数
        j = random.randint(2, int(sum_value) + 1)   # 随机生成 和
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
def minus1(sum_value, count):
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

# 连加
def add2(sum_value, count):
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
        j = random.randrange(1, sum_value+1)   # 随机生成 第二个数
        h = random.randrange(1, sum_value-1)   # 随机生成 第三个数
        l = j + i + h                              # 第二个加数
        if l < 20:
            str_temp = str(i) + ' + ' + str(j) + ' + ' +  str(h) + ' =   '
            questions += str_temp
            if(count_temp % 5 == 0):
                questions += '\n'
            count_temp += 1
            if count_temp > count:
                break

    return questions

# 连减法
def minus2(sum_value, count):
    '''
    返回指定个数（count）的计算题，以计算某数(sum_value）以内的加法
    :param sum_value: 指定某数以内（的加法）
    :param count: 随机生成多少题
    :return: 返回count个计算题
    '''
    questions = ''
    count_temp = 1   # 计数器

    while True:
        i = random.randrange(10, sum_value)     # 随机生成 第一个数
        j = random.randrange(1, sum_value+1)   # 随机生成 第二个数
        h = random.randrange(1, sum_value-1)   # 随机生成 第三个数
        l = i - j - h                                # 第二个加数
        if l >= 0:
            str_temp = str(i) + ' - ' + str(j) + ' - ' + str(h) + ' =   '
            questions += str_temp
            if(count_temp % 5 == 0):
                questions += '\n'
            count_temp += 1
            if count_temp > count:
                break

    return questions


def main():
    sum_value, count = 20, 50      # 20以内的加法,随机出100题
    title = '日期：'+ str(time.strftime('%Y-%m-%d',time.localtime(time.time()))) + '   姓名：游文熹    用时：        得分：      \n'
    # q = title + add(sum_value, count)  #  加法
    # q = title + add(sum_value, count) + minus(sum_value, count)   # 加减法
    # q = title + add2(sum_value, count)  #  连加法
    # q = title + add2(sum_value, count) + minus2(sum_value, count)  #  连加减法

    str_title = u'%d以内算术题%d题.doc'% (sum_value, count+count)
    with open(str_title, "w") as f:
        f.write(q)
    f.close()

if __name__ == '__main__':
    main()