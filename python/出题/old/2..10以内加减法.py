# !/usr/bin/env python
# -*- coding=gb2312 -*-
# Author:Hiuhung Wan

import random
import time

# �ӷ�
def add_test(sum_value, count):
    '''
    ����ָ��������count���ļ����⣬�Լ���ĳ��(sum_value�����ڵļӷ�
    :param sum_value: ָ��ĳ�����ڣ��ļӷ���
    :param count: ������ɶ�����
    :return: ����count��������
    '''
    questions = ''
    count_temp = 1   # ������

    while True:
        i = random.randrange(1, sum_value)       # ������� ��һ������
        j = random.randrange(2, sum_value + 1)   # ������� ��
        l = j - i                                # �ڶ�������
        if l > 0:
            str_temp = str(i) + ' + ' + str(l) + '' + ' = \t\t'
            questions += str_temp
            if(count_temp % 5 == 0):
                questions += '\n'
            count_temp += 1
            if count_temp > count:
                break

    return questions
# ����
def minus_test(sum_value, count):
    '''
    ����ָ��������count���ļ����⣬�Լ���ĳ��(sum_value�����ڵļӷ�
    :param sum_value: ָ��ĳ�����ڣ��ļӷ���
    :param count: ������ɶ�����
    :return: ����count��������
    '''
    questions = ''
    count_temp = 1   # ������

    while True:
        i = random.randrange(1, sum_value)       # ������� ��һ����
        j = random.randrange(2, sum_value + 1)   # ������� ��
        # l = j - i                                # �ڶ�������
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
    sum_value, count = 10, 50      # �����150�⣬10���ڵļӷ�
    title = '���ڣ�'+ str(time.strftime('%Y-%m-%d',time.localtime(time.time()))) + '   ������������    ��ʱ��        �÷֣�      \n'
    q = title +  add_test(sum_value, count) + minus_test(sum_value, count)
    str_title = u'%d���ڼӼ�������%d��.doc'% (sum_value, count+count)
    with open(str_title, "w") as f:
        f.write(q)
    f.close()

if __name__ == '__main__':
    main()