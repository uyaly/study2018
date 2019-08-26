# coding:UTF-8
import json
import collections
import re
from tool import exchange_B_D,exchange_B_H,exchange_H_B,exchange_D_H,exchange_H_D,exchange_bits

def apart_head(str):
    '''
    消息头拆分
    :param str: 消息头字符串
    :return: 拆分后的列表
    '''
    result = []
    print(str)
    print(str[32:36])
    result.append(["头-消息ID：",str[:4]])
    result.append(["头-消息体属性：" ,str[4:8]])
    str1 = exchange_H_B(str[4:8])
    # result.append(["头-消息体属性_版本标识", str1[1:2]])
    # result.append(["头-消息体属性_分包", str1[2:3]])
    # result.append(["头-消息体属性_加密方式", str1[3:6]])
    # result.append(["头-消息体属性_消息体长度_D", tool.exchange_B_D(str1[6:])])
    result.append(["头-协议版本号：" ,str[8:10]])
    result.append(["头-终端手机号：" ,str[10:30]])
    result.append(["头-消息流水号：" ,str[30:34]])
    return result

def join_head(list):
    '''
    消息头合并
    :param list:
    :return:
    '''
    result = ''
    for i in range(len(list)):
        result += list[i][1]
    print(result)
    return result

if __name__ == "__main__":

    # str = "020040550100000000013800004444004E"
    # print(apart_head(str))

    list = [['头-消息ID：', '0200'], ['头-消息体属性：', '4055'], ['头-协议版本号：', '01'], ['头-终端手机号：', '00000000013800004444'], ['头-消息流水号：', '004E']]
    print(join_head(list))