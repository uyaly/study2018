# coding:UTF-8
import json
import collections
import re

def json_txt(str):
    str = str.replace(' ', '')
    if ((str[0:2] == '7e') and (str[-2:] == '7e')) or ((str[0:2] == '7E') and (str[-2:] == '7E')) :
        result = ("消息头："+str[2:36])+ '\n'
        result += ("消息头_消息ID："+str[2:6])+ '\n'
        result += ("消息头_消息体属性："+str[6:10])+ '\n'
        result += ("消息头_协议版本号："+str[10:12])+ '\n'
        result += ("消息头_终端手机号："+str[12:32])+ '\n'
        result += ("消息头_消息流水号："+str[32:36])+ '\n'
        result += ('-' * 20) + '\n'
        result += ("消息体："+str[36:-4])  + '\n'
        # result += ("校验位："+str[-4:-2])+ '\n'
        # print("标识符:"+str[0:2])
        print("消息ID："+str[2:6])
        # print("消息体属性：+str[6:10])
        # print("协议版本号："+str[10:22])
        # print("终端手机号："+str[12:32])
        print("消息流水号："+str[32:36])
        # print("消息体："+str[36:-4])
        # print("校验位："+str[-4:-2])
        # # print("标识符:"+str[-2:])
        id_str = str[2:6]
        body_str = str[36:-4]
        # print(str(int(len(str[36:-4])/2)))
        print('-'*10)

        with open('config_bak.txt', 'r', encoding='utf-8') as file:
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
                        value_change10 = int('0x'+body_str[l:l+value], 16)
                        print(key + ': %s' % value_change10)
                        result += (key + ': %s' % value_change10)+ '\n'
                        l = l+value
                    elif '_B' in key:
                        print(body_str[l:l+value])
                        value_change2 = bin(int('0x'+body_str[l:l+value], 16))
                        if (value_change2 == '0b0'):
                            value_change2 = '0'*value*4
                        else:
                            value_change2 = value_change2[2:]   #  去掉前两位0x
                            value_change2 = "{0:>032s}".format(value_change2)   # 不足8位左侧补0
                        value_change = (' '.join(re.compile('.{4}').findall(value_change2)))    # 每隔两个数 空格一次
                        print(key + ': %s' % value_change)
                        result += (key + ': %s' % value_change)+ '\n'
                        l = l+value

                    elif isinstance(value, dict): #判断value是否是字典类型isinstance 返回True false:
                        value_list = list(value_change2[::-1])   #  字符串反转
                        for q in range(len(value.keys())):

                            bit_num = (list(value.keys())[q]).split(" ")
                            bit_name = (list(value.values())[q])
                            bits = []
                            for j in range(len(bit_num)):
                                bits += (list(value_list)[int(bit_num[j])])
                            print('【bits '+ (list(value.keys())[q])+ '】('+bit_name +')' + ':' + "".join(bits))
                            result += '【bits '+ list(value.keys())[q]+ '】'+bit_name +'' + ':' + "".join(bits)+ '\n'

                    else:
                        print(key + ': ' + body_str[l:l+value])
                        result += (key + ': ' + body_str[l:l+value])+ '\n'
                        l = l+value
            else:
                result = "请先配置"

    else :
        result = "内容不合法"
    return result
    # print(result)

if __name__ == "__main__":
    # str = "7E 80 09 00 00 01 50 02 74 94 68 00 19 4B 7E"
    # str = "7E 00 01 00 00 01 50 02 74 94 68 00 19 00 01 01 11 00 4B 7E"
    # str = "7E 80 05 00 10 01 50 02 74 94 68 00 01 00 01 02 58 00 02 01 02 03 04 05 06 00 07e0200004044034343557112ce00000000000c000201ab7d6706e23f5b001b00000000190613122316010400005daa02020000030200002504000000002a0200022b0400010000300113310113247e3 0C 0D 7E"
    # str = "7E 86 06 40 8B 01 00 00 00 00 01 38 00 00 44 44 00 01 0A 3C 61 B6 00 3D 19 08 22 19 12 34 19 08 30 19 12 38 00 05 00 00 00 01 00 00 00 01 01 CC 03 50 06 EC 08 82 64 00 00 00 00 01 00 00 00 01 01 CF 6A 6B 06 F4 AA A6 64 00 00 00 00 01 00 00 00 01 01 D5 C4 18 06 F3 A9 28 0A 03 00 04 00 05 00 06 07 00 00 00 00 00 01 00 00 00 01 01 D8 36 52 06 DE 33 FE 0A 03 00 04 00 05 00 06 07 00 00 00 00 00 01 00 00 00 01 01 CA DA 51 06 D4 0F 9D 0A 03 00 04 00 05 00 06 07 00 00 00 00 A7 7E"
    str = "7E 02 00 40 05 01 00 00 00 00 01 38 00 00 44 44 00 0C 00 80 00 00 00 00 10 13 06 CE F9 C0 01 D1 D6 24 00 00 00 00 00 00 19 08 23 10 55 28 01 04 00 01 2F 50 02 02 00 00 03 02 00 00 31 01 00 14 04 00 00 00 00 30 01 36 F0 01 03 F1 0A 30 8C AC 53 24 4F 18 00 74 8C F2 01 00 F3 02 03 63 F4 04 00 07 F1 FF E1 01 8B 00 7E"
    # str = "7E 00 01 40 05 01 00 00 00 00 01 38 00 00 44 44 00 0A 00 04 86 06 00 00 7E "
    json_txt(str)