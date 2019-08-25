# coding:UTF-8
import json
import collections
import re

# def json_txt(str):
#     str = str.replace(' ', '')
#     if ((str[0:2] == '7e') and (str[-2:] == '7e')) or ((str[0:2] == '7E') and (str[-2:] == '7E')) :
#         result = ("消息ID："+str[2:6])+ '\n'
#         result += ("消息体属性："+str[6:10])+ '\n'
#         result += ("协议版本号："+str[10:12])+ '\n'
#         result += ("终端手机号："+str[12:32])+ '\n'
#         result += ("消息流水号："+str[32:36])+ '\n'
#         result += ("消息体："+str[36:-4])+ '\n'
#         result += ("校验位："+str[-4:-2])+ '\n'
#         result += ('-'*20)+ '\n'
#         # print("________说明  _D:十进制,_B:二进制________")
#         print("标识符:"+str[0:2])
#         print("消息ID："+str[2:6])
#         print("消息体属性："+str[6:10])
#         print("协议版本号："+str[10:12])
#         print("终端手机号："+str[12:32])
#         print("消息流水号："+str[32:36])
#         print("消息体："+str[36:-4])
#         print("校验位："+str[-4:-2])
#         # print("标识符:"+str[-2:])
#         id_str = str[2:6]
#         body_str = str[26:-4]
#         # print('-'*10)
#
#         with open('config.txt', 'r', encoding='utf-8') as file:
#             content = file.read()
#             dic = json.loads(content, object_pairs_hook=collections.OrderedDict)
#             if id_str in dic:
#                 body_dic = (dic[id_str])
#                 keylist_dic = body_dic.keys()
#                 valuelist_dic = list(body_dic.values())
#                 l = 0
#                 for p in range(len(keylist_dic)):
#                     key = list(keylist_dic)[p]
#                     value = list(valuelist_dic)[p]
#                     if '_D' in key:
#                         value_change10 = int('0x'+body_str[l:l+value], 16)
#                         print(key + ': %s' % value_change10)
#                         result += (key + ': %s' % value_change10)+ '\n'
#                         l = l+value
#                     elif '_B' in key:
#                         print(body_str[l:l+value])
#                         value_change2 = bin(int('0x'+body_str[l:l+value], 16))
#                         if (value_change2 == '0b0'):
#                             value_change2 = '0'*value*4
#                         else:
#                             value_change2 = value_change2[2:]   #  去掉前两位0x
#                             value_change2 = "{0:>032s}".format(value_change2)   # 不足8位左侧补0
#                         value_change = (' '.join(re.compile('.{4}').findall(value_change2)))    # 每隔两个数 空格一次
#                         print(key + ': %s' % value_change)
#                         result += (key + ': %s' % value_change)+ '\n'
#                         l = l+value
#
#                     elif isinstance(value, dict): #判断value是否是字典类型isinstance 返回True false:
#                         value_list = list(value_change2[::-1])   #  字符串反转
#                         for q in range(len(value.keys())):
#
#                             bit_num = (list(value.keys())[q]).split(" ")
#                             bit_name = (list(value.values())[q])
#                             bits = []
#                             for j in range(len(bit_num)):
#                                 bits += (list(value_list)[int(bit_num[j])])
#                             print('【bits '+ (list(value.keys())[q])+ '】('+bit_name +')' + ':' + "".join(bits))
#                             result += '【bits '+ (list(value.keys())[q])+ '】('+bit_name +')' + ':' + "".join(bits)+ '\n'
#
#                     else:
#                         # print(key + ': ' + body_str[l:l+value])
#                         result += (key + ': ' + body_str[l:l+value])+ '\n'
#                         l = l+value
#             else:
#                 result = "请先配置，再分析"
#
#     else :
#         result = "内容不合法"
#     return result
#     # print(result)

def json_txt(str):
    str = str.replace(' ', '')
    if ((str[0:2] == '7e') and (str[-2:] == '7e')) or ((str[0:2] == '7E') and (str[-2:] == '7E')) :
        result = []
        result.append(["头-消息ID：",str[2:6]])
        result.append(["头-消息体属性_版本：" ,str[6:10]])
        result.append(["头-消息体属性_加密：" ,str[6:10]])
        result.append(["头-消息体属性_长度：" ,str[6:10]])
        result.append(["头-协议版本号：" ,str[10:12]])
        result.append(["头-终端手机号：" ,str[12:32]])
        result.append(["头-消息流水号：" ,str[32:36]])
        # result.append(["消息体：" ,str[36:-4]])
        # result.append(["校验位：" ,str[-4:-2]])
        # result.append(['-'*20) , '\n'
        id_str = str[2:6]
        body_str = str[36:-4]
        # print('-'*10)

        with open('config.txt', 'r', encoding='utf-8') as file:
            content = file.read()
            try:
                dic = json.loads(content, object_pairs_hook=collections.OrderedDict)
            except:
                result = "配置文件读取失败"
                pass

            if id_str in dic:
                body_dic = (dic[id_str])
                keylist_dic = body_dic.keys()
                valuelist_dic = list(body_dic.values())
                l = 0
                for p in range(len(keylist_dic)):
                    key = list(keylist_dic)[p]
                    value = list(valuelist_dic)[p]
                    if '_D' in key:
                        value_D = exchange_D(body_str[l:l+value])
                        # print(key+':',value_D)
                        result.append([key+':',value_D])
                        l = l + value

                    elif '_B' in key:
                        value_b = exchange_B(body_str[l:l+value], value)
                        value_B = (' '.join(re.compile('.{4}').findall(value_b)))    # 每隔两个数 空格一次
                        # print(key + ':', value_B)
                        result.append([key + ':', value_B])
                        l = l + value

                    elif isinstance(value, dict): #判断value是否是字典类型isinstance 返回True false
                        bitslist = exchange_bits(value_b, value)
                        # print(bitslist)
                        result.append(bitslist)

                    else:
                        result.append([key + ': ', body_str[l:l+value]])
                        # print(key + ': ', body_str[l:l+value])
                        l = l+value
            else:
                result = "请先配置，再分析"

    else :
        result = "内容不合法"
    return result

def exchange_D(str):
    '''
    转十进制
    :return:
    '''
    value_D = int('0x'+ str, 16)
    return value_D

def exchange_B(str, value):
    '''
    转2进制
    :return:
    '''
     # print(body_str[l:l+value])
    value_b = bin(int('0x'+ str, 16))
    if (value_b == '0b0'):
        value_b = '0'* value *4
    else:
        value_b = value_b[2:]   #  去掉前两位0x
        value_b = "{0:>032s}".format(value_b)   # 不足8位左侧补0

    return value_b


def exchange_bits(value_b, value):
    ll = []
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


if __name__ == "__main__":

    str = "7E 02 00 40 55 01 00 00 00 00 01 38 01 80 42 79 00 4E 00 00 00 00 00 00 10 11 00 00 00 00 00 00 00 00 00 00 00 00 00 00 19 08 23 10 55 28 01 04 00 01 2F 50 02 02 00 00 03 02 00 00 31 01 00 14 04 00 00 00 00 30 01 36 F0 01 03 F1 0A 30 8C AC 53 24 4F 18 00 74 8C F2 01 00 F3 02 03 63 F4 04 00 07 F1 FF E1 01 8B EC 7E"
    # str = "7E 80 04 00 10 01 50 02 74 94 68 00 01 12 01 00 0D 7E"
    json_txt(str)