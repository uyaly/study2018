# !/usr/bin/env python
# -*- coding=gb2312 -*-

import time
from random import randint
sym = [' + ', ' - ']

# 加法
def base_plus(pmin, pmax, num):
    '''
    pmin,pmax:加数、被加数、和最小最大值
    num:题目数
    '''
    num_temp = 1   # 计数器
    result = []
    while True:
        plus1 = randint(pmin, pmax)
        plus2 = randint(pmin, pmax)
        if (plus1 + plus2 <= pmax):
            # plus：加法算式，rjust(2)：按2位数右对齐
            plus = str(plus1).rjust(2) + ' + ' + str(plus2).rjust(2) + ' =   '
            result.append(plus)
            num_temp += 1
        if num_temp > num:
            break
    return result

def base_minus(mmin, mmax, num):
    '''
    mmin,mmax:减法转换成加法后，加数、被加数最小最大值
    minussum:减数+减数
    num:题目数
    '''
    num_temp = 1   # 计数器
    result = []

    while True:
        minus1 = randint(mmin, mmax)
        minus2 = randint(mmin+1, mmax)
        sum = minus1 + minus2
        if (sum <= mmax):
            minus = str(sum).rjust(2) + ' - ' + str(minus1).rjust(2) + ' =   '
            if minus not in result:
                result.append(minus)
                num_temp += 1
        if num_temp > num:
            break
    return result

# 类型1算式：... +/- ... +/- ...
def type1_str(tmin, tmax, summin, summax, num):
    '''
    summin,summax:允许总和的最小最大值
    '''
    num_temp = 1   # 计数器
    result = []
    while True:
        sym1 = sym[randint(0, 1)]
        sym2 = sym[randint(0, 1)]
        if sym1 == ' + ' and sym2 == ' + ':
            sum_ = randint(summin + 2, summax)
            first = randint(summin, sum_ - 2)
            second = sum_ - first
            second = randint(summin, second - 1)
            third = sum_ - first - second
        elif sym1 == ' + ' and sym2 == ' - ':
            sum_ = randint(summin + 1, summax)
            first = randint(summin, sum_ - 1)
            second = sum_ - first
            third = randint(summin, sum_)
        elif sym1 == ' - ' and sym2 == ' + ':
            first = randint(summin + 1, summax)
            second = randint(summin, first)
            third = randint(first - second, summax)
        elif sym1 == ' - ' and sym2 == ' - ':
            first = randint(summin + 2, summax)
            second = randint(summin, first)
            third = first - second
            third = randint(summin, third)
        # 判断第一个值的范围
        if (first>tmin and first<tmax ):
            arithmetic = str(first).rjust(2) + sym1 + str(second).rjust(2) + sym2 + str(third).rjust(2) + ' =     '
            result.append(arithmetic)
            num_temp += 1
        if num_temp > num:
            break
    return result