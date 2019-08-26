# coding:UTF-8
import json
import collections
import re

def json_txt(str):
    str = str.replace(' ', '')
    if ((str[0:2] == '7e') and (str[-2:] == '7e')) or ((str[0:2] == '7E') and (str[-2:] == '7E')) :
        result = []
        result2 = []
        result.append(["消息ID：",str[2:6]])
        result.append (["消息体属性：",str[6:10]])
        # result.append (["消息体长度：",str[6:10]])
        result.append (["协议版本号：",str[10:12]])
        result.append (["终端手机号：",str[12:32]])
        result.append (["消息流水号：",str[32:36]])
        result.append (["消息体：",'-'*10])
        # result.append (["消息体：",str[36:-4]])
        # result.append (["校验位：",str[-4:-2]])
        id_str = str[2:6]
        body_str = str[36:-4]
        # print('-'*10)

        with open('config.txt', 'r', encoding='utf-8') as file:
            content = file.read()
            dic = json.loads(content, object_pairs_hook=collections.OrderedDict)
            if id_str in dic:
                body_dic = (dic[id_str])
                keylist_dic = body_dic.keys()
                valuelist_dic = list(body_dic.values())
                l = 0
                for p in range(len(keylist_dic)):
                    key = list(keylist_dic)[p]
                    value = list(valuelist_dic)[p]
                    if '_D' in key:
                        # value_change10 = int('0x'+body_str[l:l+value], 16)
                        value_change10 = int(body_str[l:l+value], 16)
                        # print(key + ': %s' % value_change10)

                        result.append ([key + ':', (value_change10)])
                        l = l+value
                    elif '_B' in key:
                        # print(body_str[l:l+value])
                        value_change2 = bin(int('0x'+body_str[l:l+value], 16))
                        if (value_change2 == '0b0'):
                            value_change2 = '0'* value *4
                        else:
                            value_change2 = value_change2[2:]   #  去掉前两位0x
                            value_change2 = "{0:>032s}".format(value_change2)   # 不足8位左侧补0
                        value_change = (' '.join(re.compile('.{4}').findall(value_change2)))    # 每隔两个数 空格一次
                        # print(key + ': %s' % value_change)
                        result.append ([key + ':', value_change])
                        l = l+value

                    elif isinstance(value, dict): #判断value是否是字典类型isinstance 返回True false:
                        value_list = list(value_change2[::-1])   #  字符串反转
                        for q in range(len(value.keys())):
                            bit_num = (list(value.keys())[q]).split(" ")
                            bit_name = (list(value.values())[q])
                            bits = []
                            for j in range(len(bit_num)):
                                bits.append (list(value_list)[int(bit_num[j])])
                            # print('【bits '+ (list(value.keys())[q])+ '】('+bit_name +')' + ':' + "".join(bits))
                            result2.append([key+'['+ (list(value.keys())[q])+ ']'+bit_name ,"".join(bits)])

                    else:
                        # print(key + ': ' + body_str[l:l+value])
                        result.append ([key + ': ' , body_str[l:l+value]])
                        l = l+value
            else:
                result = "请先配置，再分析"

    else :
        result = "内容不合法"
    # print(result)
    return [result, result2]

if __name__ == "__main__":

    str = "7E 02 00 40 55 01 00 00 00 00 01 38 01 80 42 79 00 4E 00 80 00 00 00 00 10 11 00 00 00 00 00 00 00 00 00 00 00 00 00 00 19 08 23 10 55 28 01 04 00 01 2F 50 02 02 00 00 03 02 00 00 31 01 00 14 04 00 00 00 00 30 01 36 F0 01 03 F1 0A 30 8C AC 53 24 4F 18 00 74 8C F2 01 00 F3 02 03 63 F4 04 00 07 F1 FF E1 01 8B EC 7E"
    # str = "7E 80 04 00 10 01 50 02 74 94 68 00 01 12 01 00 0D 7E"
    json_txt(str)