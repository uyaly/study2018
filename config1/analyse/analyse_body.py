# coding:UTF-8
import json
import collections
import re
from tool import exchange_B_D,exchange_B_H,exchange_H_B,exchange_D_H,exchange_H_D,exchange_bits

def apart_body(str, dic):
    keylist_dic = body_dic.keys()
    valuelist_dic = list(body_dic.values())
    l = 0
    for p in range(len(keylist_dic)):
        key = list(keylist_dic)[p]
        value = list(valuelist_dic)[p]
        if '_D' in key:
            value_D = exchange_H_D(body_str[l:l + value])
            # print(key+':',value_D)
            result.append([key + ':', value_D])
            l = l + value

        elif '_B' in key:
            value_b = exchange_B(body_str[l:l + value], value)
            value_B = (' '.join(re.compile('.{4}').findall(value_b)))  # 每隔两个数 空格一次
            # print(key + ':', value_B)
            result.append([key + ':', value_B])
            l = l + value

        elif isinstance(value, dict):  # 判断value是否是字典类型isinstance 返回True false
            bitslist = exchange_bits(value_b, value)
            # print(bitslist)
            result.append(bitslist)

        else:
            result.append([key + ': ', body_str[l:l + value]])
            # print(key + ': ', body_str[l:l+value])
            l = l + value




if __name__ == "__main__":

    str = "008000000000101306CEF9C001D1D624000000000000190823105528010400012F500202000003020000310100140400000000300136F00103F10A308CAC53244F1800748CF20100F3020363F4040007F1FFE1018B"
    # str = "7E 80 04 00 10 01 50 02 74 94 68 00 01 12 01 00 0D 7E"
    apart_body(str,)