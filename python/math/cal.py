# !/usr/bin/env python
# -*- coding=gb2312 -*-

import time
from random import randint
sym = [' + ', ' - ']

# �ӷ�
def base_plus(pmin, pmax, num):
    '''
    pmin,pmax:������������������С���ֵ
    num:��Ŀ��
    '''
    num_temp = 1   # ������
    result = []
    while True:
        plus1 = randint(pmin, pmax)
        plus2 = randint(pmin, pmax)
        if (plus1 + plus2 <= pmax):
            # plus���ӷ���ʽ��rjust(2)����2λ���Ҷ���
            plus = str(plus1).rjust(2) + ' + ' + str(plus2).rjust(2) + ' =   '
            result.append(plus)
            num_temp += 1
        if num_temp > num:
            break
    return result

def base_minus(mmin, mmax, num):
    '''
    mmin,mmax:����ת���ɼӷ��󣬼�������������С���ֵ
    num:��Ŀ��
    '''
    num_temp = 1   # ������
    result = []
    while True:
        minus1 = randint(mmin, mmax)
        minus2 = randint(mmin, mmax)
        sum = minus1 + minus2
        if (sum <= mmax):
            minus = str(sum).rjust(2) + ' - ' + str(minus1).rjust(2) + ' =   '

            result.append(minus)
            num_temp += 1
        if num_temp > num:
            break
    return result

# ����1��ʽ��... +/- ... +/- ...
def type1_str(tmin, tmax, num):
    '''
    summin,summax:�����ܺ͵���С���ֵ
    '''
    num_temp = 1   # ������
    result = []
    while True:
        sym1 = sym[randint(0, 1)]
        sym2 = sym[randint(0, 1)]
        if sym1 == ' + ' and sym2 == ' + ':
            sum_ = randint(tmin + 2, tmax)
            first = randint(tmin, sum_ - 2)
            second = sum_ - first
            second = randint(tmin, second - 1)
            third = sum_ - first - second
        elif sym1 == ' + ' and sym2 == ' - ':
            sum_ = randint(tmin + 1, tmax)
            first = randint(tmin, sum_ - 1)
            second = sum_ - first
            third = randint(tmin, sum_)
        elif sym1 == ' - ' and sym2 == ' + ':
            first = randint(tmin + 1, tmax)
            second = randint(tmin, first)
            third = randint(first - second, tmax)
        elif sym1 == ' - ' and sym2 == ' - ':
            while 1:
                first = randint(tmin + 2, tmax)
                second = randint(tmin, first)
                third = first - second
                if (third>=tmin):
                    third = randint(tmin, third)
                    break
                else:
                    continue
        # �жϵ�һ��ֵ�ķ�Χ
        arithmetic = str(first).rjust(2) + sym1 + str(second).rjust(2) + sym2 + str(third).rjust(2) + ' =     '
        if arithmetic not in result:
            result.append(arithmetic)
            num_temp += 1
        if num_temp > num:
            break
    return result