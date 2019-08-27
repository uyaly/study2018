# coding:UTF-8
import json
import collections
import re

def exchange_B_D(strB):
    '''
    二进制转十进制
    :param str:
    :return:
    '''
    # value_D = (int(str,2))
    # print(value_D)
    value_D = str(int(strB,2))
    return value_D

def exchange_D_H(str):
    '''
    十进制转十六进制
    :return:
    '''
    value_H = (hex(int(str)))[2:]
    return value_H

def exchange_H_D(str):
    '''
    十六进制转十进制
    :return:
    '''
    str = str.replace(' ', '')
    value_D = int('0x'+ str, 16)
    return value_D

def exchange_H_B(str):
    '''
    16进制转2进制
    :return:
    '''
     # print(body_str[l:l+value])
    str = str.replace(' ', '')
    l = len(str)*4
    value_b = bin(int('0x'+ str, 16))
    if (value_b == '0b0'):
        value_b = '0'* l
    else:
        value_b = value_b[2:]   #  去掉前两位0x
        value_b = value_b.zfill(l)
        # value_b = "{0:>0ls}".format(value_b)   # 不足32位左侧补0
    return value_b

def exchange_B_H(str):
    '''
    2进制转16进制
    :return:
    '''
    str = str.replace(' ', '')
    value_H = hex(int(str, 2))[2:]
    return value_H

def exchange_bits(value_b):
    ll = []
    # str = str.replace(' ', '')
    value_list = list(value_b[::-1])   #  字符串反转
    for q in range(len(value.keys())):
        bit_num = (list(value.keys())[q]).split(" ")
        bit_name = (list(value.values())[q])
        bits = []
        for j in range(len(bit_num)):
            bits += (list(value_list)[int(bit_num[j])])
        # print('[bit '+ list(value.keys())[q]+ ']' + bit_name + ':', "".join(bits))

        ll.append(['[bit '+ list(value.keys())[q]+ ']'+bit_name + ':', "".join(bits)])
    return ll

def apart_str(result, num):
    resultArr = re.findall('.{' + str(num) + '}', result)
    resultArr.append(result[(len(resultArr) * num):])
    return resultArr

def x_o_r(resultArr):
    '''
    计算校验位
    :param result: 字符串
    :param num: 按几位拆分字符串
    :return: 两两异或，返回16进制数
    '''
    c = int('00', 16)
    for i in range(0, len(resultArr) - 1):
        a = int(resultArr[i], 16)
        c = hex(a ^ c)[2:]
        c = int(c, 16)
        # print ("a^b:%d"% c)
    c = hex(c)[2:]
    return c

if __name__ == "__main__":

    # str = "7E 02 00 40 55 01 00 00 00 00 01 38 01 80 42 79 00 4E 00 00 00 00 00 00 10 11 00 00 00 00 00 00 00 00 00 00 00 00 00 00 19 08 23 10 55 28 01 04 00 01 2F 50 02 02 00 00 03 02 00 00 31 01 00 14 04 00 00 00 00 30 01 36 F0 01 03 F1 0A 30 8C AC 53 24 4F 18 00 74 8C F2 01 00 F3 02 03 63 F4 04 00 07 F1 FF E1 01 8B EC 7E"
    # str = "7E 80 04 00 10 01 50 02 74 94 68 00 01 12 01 00 0D 7E"
    # json_txt(str)

    # print(exchange_D_H("10"))
    # print(exchange_H_D("00 00 10 11"))
    print(exchange_B_D("0001010101"))
    # print(exchange_H_B("00 00 10 11"))
    # print(exchange_B_H("0000 0000 0000 0000 0001 0000 0001 0001"))

