# !/usr/bin/env python
# -*- coding=gb2312 -*-

import random
import time

# �ӷ�
def base_plus(min_value, max_value, count):
    '''
    ����ָ��������count���ļ����⣬�Լ���ĳ��(sum_value�����ڵļӷ�
    :param sum_value: ָ��ĳ�����ڣ��ļӷ���
    :param count: ������ɶ�����
    :return: ����count��������
    '''
    questions = []
    count_temp = 1   # ������

    while True:
        i = random.randint(int(min_value), int(max_value))       # ������� ��һ������
        j = random.randint(2, int(max_value) + 1)   # ������� ��
        l = j - i                                # �ڶ�������
        if l > 0:
            str_temp = str(i) + ' + ' + str(l) + '' + ' = \t\t'
            questions.append(str_temp)
            # if(count_temp % 5 == 0):
            #     questions += '\n'
            count_temp += 1
            if count_temp > count:
                break

    return questions

# ����
def base_minus(min_value, max_value, count):
    '''
    ����ָ��������count���ļ����⣬�Լ���ĳ��(sum_value�����ڵļӷ�
    :param sum_value: ָ��ĳ�����ڣ��ļӷ���
    :param count: ������ɶ�����
    :return: ����count��������
    '''
    questions = []
    count_temp = 1   # ������

    while True:
        i = random.randrange(int(min_value), int(max_value))       # ������� ��һ����
        j = random.randrange(2, max_value + 1)   # ������� ��
        # l = j - i                                # �ڶ�������
        if i > j:
            str_temp = str(i) + ' - ' + str(j) + '' + ' = \t\t'
            questions.append(str_temp)
            # if(count_temp % 5 == 0):
            #     questions += '\n'
            count_temp += 1
            if count_temp > count:
                break

    return questions

def main():
    sum_value, count = 20, 50      # 20���ڵļӷ�,�����100��
    title = '���ڣ�'+ str(time.strftime('%Y-%m-%d',time.localtime(time.time()))) + '   ������������    ��ʱ��        �÷֣�      \n'
    # q = title + add(sum_value, count)  #  �ӷ�
    # q = title + add(sum_value, count) + minus(sum_value, count)   # �Ӽ���
    # q = title + add2(sum_value, count)  #  ���ӷ�
    # q = title + add2(sum_value, count) + minus2(sum_value, count)  #  ���Ӽ���

    str_title = u'%d����������%d��.doc'% (sum_value, count+count)
    with open(str_title, "w") as f:
        f.write(q)
    f.close()

if __name__ == '__main__':
    main()