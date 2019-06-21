# !/usr/bin/env python
# -*- coding=gb2312 -*-

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
        plus2 = randint(2, pmax + 1)
        if (plus1 + plus2 <= pmax):
            # plus：加法算式，rjust(2_0)：按2位数右对齐
            plus = str(plus1).rjust(2) + ' + ' + str(plus2).rjust(2) + ' =   '
            result.append(plus)
            num_temp += 1
        if num_temp > num:
            break
    return result
# 减法
def base_minus(mmin, mmax, num):
    '''
    mmin,mmax:减法转换成加法后，加数、被加数最小最大值
    num:题目数
    '''
    num_temp = 1   # 计数器
    result = []
    while True:
        minus1 = randint(mmin, mmax)
        minus2 = randint(2, mmax + 1)
        sum = minus1 + minus2
        if (sum <= mmax):
            minus = str(sum).rjust(2) + ' - ' + str(minus1).rjust(2) + ' =   '
            result.append(minus)
            num_temp += 1
        if num_temp > num:
            break
    return result
# 乘法
def base_multi(multimin, multimax, num):
    '''
    multimin,multimax:乘数、被乘数最小最大值
    '''
    # multi：乘法算式
    num_temp = 1   # 计数器
    result = []
    while True:
        multi1 = randint(multimin, multimax)
        multi2 = randint(multimin, multimax)
        multi = str(multi1).rjust(2) + ' x ' + str(multi2).rjust(2) + ' =   '
        result.append(multi)
        num_temp += 1
        if num_temp > num:
            break
    return result
# 除法
def base_div(divmin, divmax, num):
    '''
    divmin,divmax:除法转换成乘法后，乘数、被乘数最小最大值
    '''
    # div：除法算式
    num_temp = 1   # 计数器
    result = []
    while True:
        div1 = randint(divmin, divmax)
        div2 = randint(divmin, divmax)
        divmulti = div1 * div2
        div = str(divmulti).rjust(2) + ' / ' + str(div1).rjust(2) + ' =   '
        result.append(div)
        num_temp += 1
        if num_temp > num:
            break
    return result
# 类型1算式：... +/- ... +/- ...
def type1_str(summin, summax, num):
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
            if (third != 0):
                third = randint(summin, third)

        arithmetic = str(first).rjust(2) + sym1 + str(second).rjust(2) + sym2 + str(third).rjust(2) + ' =     '
        if arithmetic not in result:
            result.append(arithmetic)
            num_temp += 1
        if num_temp > num:
            break
    return result

# 类型2算式：... +/- ... x ...
def type2_str(multimin, multimax, summin, summax, num):
    '''
    multimin,multimax:乘数、被乘数最小最大值
    summin,summax:允许总和的最小最大值
    '''
    num_temp = 1   # 计数器
    result = []
    while True:
        sym1 = sym[randint(0, 1)]
        second = randint(multimin, multimax)
        third = randint(multimin, multimax)
        multi = second * third

        if sym1 == ' + ':
            first = randint(summin, summax - multi)
        else:
            first = randint(multi, summax)

        arithmetic = str(first).rjust(2) + sym1 + str(second).rjust(2) + ' x ' + str(third).rjust(2) + ' =     '
        # print arithmetic
        # return arithmetic
        if arithmetic not in result:
            result.append(arithmetic)
            num_temp += 1
        if num_temp > num:
            break
    return result


# 类型3算式：(... +/- ...) / ...
def type3_str(multimin, multimax, summin, summax, num):
    '''
    multimin,multimax:乘数、被乘数最小最大值
    summin,summax:允许总和的最小最大值
    '''
    num_temp = 1   # 计数器
    result = []
    while True:
        sym1 = sym[randint(0, 1)]
        second = randint(multimin, multimax)
        third = randint(multimin, multimax)
        multi = second * third

        if sym1 == '+':
            first = randint(summin, multi)
            second = multi - first
        else:
            second = randint(summin, summax - multi)
            first = multi + second

        arithmetic = '(' + str(first).rjust(2) + sym1 + str(second).rjust(2) + ')' + '/' + str(third).rjust(2) + ' =     '
        if arithmetic not in result:
            result.append(arithmetic)
            num_temp += 1
        if num_temp > num:
            break
    return result