# coding:UTF-8
import json
import collections
import re
# 发送时，每次需要注册新的手机号码，就需要json每次提示mobileTel的value进行发送
#遍历json文件所有的key对应的value
dic ={}
def json_txt1(body_dic):
    if isinstance(body_dic,dict): #判断是否是字典类型isinstance 返回True false
        for key in body_dic:
            if isinstance(body_dic[key],dict):#如果dic_json[key]依旧是字典类型
                # print("****key--：%s value--: %s"%(key,body_dic[key]))
                json_txt1(body_dic[key])
                dic[key] = body_dic[key]
            else:
                # print("****key--：%s value--: %s"%(key,body_dic[key]))
                dic[key] = body_dic[key]
    print("dic:::",dic)
    return dic

def json_txt(str_1):
    srr1 = str_1
    id_str = srr1[2:6]
    body_str = srr1[26:-4]
    # print("标识符:"+str1[0:2.txt])
    # print(str1)
    # print("消息ID："+id_str)
    # print("消息体长度："+str1[6:10])
    # print("终端ID："+str1[10:22])
    # print("消息流水号："+str1[22:26])
    # print("消息体："+str1[26:-4])
    # print("校验位："+str1[-4:-2])
    # # print("标识符:"+str1[-2.txt:])

    print('-'*10)

    content = None
    with open('1.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        date_json = json.loads(content, object_pairs_hook=collections.OrderedDict)
        body_dic = (date_json[id_str])
        # print(body_dic)
        key_list = body_dic.keys()
        # print(key_list)
        l = 0
        for p in range(len(key_list)):
            value = list(body_dic.values())[p]
            if '*' in list(key_list)[p]:
                value_list = json_txt1(value)
                value = (value_list['LONG'])
                print(value)
            elif '_D' in list(key_list)[p]:
                value_change10 = int('0x'+body_str[l:l+value], 16)
                print(list(key_list)[p] + ': %s' % value_change10)
            elif '_B' in list(key_list)[p]:
                # print(body_str[l:l+value])
                value_change2 = bin(int('0x'+body_str[l:l+value], 16))
                if (value_change2 == '0b0'):
                     value_change2 = '0'*value*4
                else:
                     value_change2 = value_change2[2:]
                value_change2 = (' '.join(re.compile('.{4}').findall(value_change2)))
                print(list(key_list)[p] + ': %s' % value_change2)
            else:
                print(list(key_list)[p] + ': ' + body_str[l:l+value])
            l = l+value

if __name__ == "__main__":
     # str1 = "7E 80 09 00 00 01 50 02 74 94 68 00 19 4B 7E"
     # str1 = "7E 00 01 00 00 01 50 02 74 94 68 00 19 00 01 01 11 00 4B 7E"
     # str1 = "7E 80 05 00 10 01 50 02 74 94 68 00 01 00 01 02 58 00 02 01 02 03 04 05 06 00 03 0C 0D 7E"
     str1 = "7e0200004044034343557112ce00000000000c000201ab7d6706e23f5b001b00000000190613122316010400005daa02020000030200002504000000002a0200022b0400010000300113310113247e"
     str1 = str1.replace(' ', '')
     json_txt(str1)
