# coding:UTF-8
import json
import collections
import re
from tool import exchange_B_D,exchange_B_H,exchange_H_B,exchange_D_H,exchange_H_D,exchange_bits
import analyse_head as head
import analyse_body as body

def apart(str):
    '''
    报文拆分成列表
    :param str: 需要拆分的报文
    :return:列表
    '''
    str = str.replace(' ', '')
    list = []
    if ((str[0:2] == '7e') and (str[-2:] == '7e')) or ((str[0:2] == '7E') and (str[-2:] == '7E')):
        list.append(["标识位：", str[0:2]])
        list.append(["消息头：", str[2:36]])
        head_str = str[2:36]
        list.append(["消息体：", str[36:-4]])
        body_str = str[36:-4]
        list.append(["校验位：", str[-4:-2]])
        list.append(["标识位：", str[-2:]])
        id_str = str[2:6]
        # print(list[1])  #消息头
        # print(list[2])  #消息体
        # print(list)
        with open('config.txt', 'r', encoding='utf-8') as file:
            content = file.read()
            try:
                dic = json.loads(content, object_pairs_hook=collections.OrderedDict)
                result = []
                if id_str in dic:
                    body_dic = (dic[id_str])
                    result_head = head.apart_head(head_str)
                    result = result_head
                    result_body = body.apart_body(body_str, body_dic)
                    result += result_body
                else:
                    result = "请先配置"+id_str+"，再分析"
            except:
                result = "配置文件读取失败"
                pass
    else:
        result = "报文内容不合法"
    # print(result)
    return result

def join(list):
    '''
    列表合并成报文
    :param list: 列表
    :return: 报文
    '''
    result = ''
    for i in range(len(list)):
        result += list[i]
    # print(result)

    # for k in range(0,len(result)):
    #     for l in range(1,len(result)):
    #         a = result[k:k+2]
    #         b = result[l:l+2]
    #         x_o_r(a, b)
    resultArr = re.findall('.{2}', result)
    resultArr.append(result[(len(resultArr)*2):])
    print(resultArr)
    c=int(0,16)
    for i in range(0,len(resultArr),2):
        a=int(resultArr[i],16)
        print(a)
        b=int(resultArr[i+1],16)
        print(b)
        d = x_o_r(a, b)
        print (d)
        print(type.d)
        c = x_o_r(c, d)
        print (c)
    print(c)

    result = '7E' +result+  '007E'
    result = ' '.join(re.compile('.{2}').findall(result))  # 隔两位一个空格
    return result


def x_o_r(byte1, byte2):  # 传入两个数，并返回它们的异或结果，结果为16进制数
    return hex(byte1 ^ byte2)[2:]

if __name__ == "__main__":
    str = "7E 80 01 40 05 01 00 00 00 00 01 38 00 00 44 44 00 0A 00 4E 02 00 00 00 7E "
    # str = "7E 02 00 40 55 01 00 00 00 00 01 38 00 00 44 44 00 4E 00 80 00 00 00 00 10 13 06 CE F9 C0 01 D1 D6 24 00 00 00 00 00 00 19 08 23 10 55 28 01 04 00 01 2F 50 02 02 00 00 03 02 00 00 31 01 00 14 04 00 00 00 00 30 01 36 F0 01 03 F1 0A 30 8C AC 53 24 4F 18 00 74 8C F2 01 00 F3 02 03 63 F4 04 00 07 F1 FF E1 01 8B EC 7E"
    apart(str)
    # list=[['标识位：', '7E'], ['消息头：', '020040550100000000013800004444004E'], ['消息体：', '008000000000101306CEF9C001D1D624000000000000190823105528010400012F500202000003020000310100140400000000300136F00103F10A308CAC53244F1800748CF20100F3020363F4040007F1FFE1018B'], ['校验位：', 'EC'], ['标识位：', '7E']]
    # join(list)
