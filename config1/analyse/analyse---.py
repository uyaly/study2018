# coding:UTF-8
import json
import collections
import re
import tool


def analyse():
    str = str.replace(' ', '')
    list = []
    if ((str[0:2] == '7e') and (str[-2:] == '7e')) or ((str[0:2] == '7E') and (str[-2:] == '7E')):
        list.append(["标识位：", str[0:2]])
        list.append(["消息头：", str[2:36]])
        list.append(["消息体：", str[36:-4]])
        list.append(["校验位：", str[-4:-2]])
        list.append(["标识位：", str[-2:]])
        print(list[1])  #消息头
        print(list[2])  #消息体
        print(list[3])  #校验位
        result = [list[1],list[2],list[3]]
        return  result
    else:
        result = "内容不合法"
    return result


def analyse():
    str = str.replace(' ', '')

def json_txt(str):
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
                        value_D = exchange_H_D(body_str[l:l+value])
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



if __name__ == "__main__":

    # str = "7E 02 00 40 55 01 00 00 00 00 01 38 01 80 42 79 00 4E 00 00 00 00 00 00 10 11 00 00 00 00 00 00 00 00 00 00 00 00 00 00 19 08 23 10 55 28 01 04 00 01 2F 50 02 02 00 00 03 02 00 00 31 01 00 14 04 00 00 00 00 30 01 36 F0 01 03 F1 0A 30 8C AC 53 24 4F 18 00 74 8C F2 01 00 F3 02 03 63 F4 04 00 07 F1 FF E1 01 8B EC 7E"
    # str = "7E 80 04 00 10 01 50 02 74 94 68 00 01 12 01 00 0D 7E"
    # json_txt(str)