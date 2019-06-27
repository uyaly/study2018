# coding:UTF-8
import json
import collections
import re

def json_txt(str):
     # print("标识符:"+str[0:2.txt])
     print("消息ID："+str[2:6])
     print("消息体长度："+str[6:10])
     print("终端ID："+str[10:22])
     print("消息流水号："+str[22:26])
     print("消息体："+str[26:-4])
     print("校验位："+str[-4:-2])
     # # print("标识符:"+str[-2.txt:])
     id_str = str[2:6]
     body_str = str[26:-4]
     print('-'*10)

     content = None
     with open('3.txt', 'r', encoding='utf-8') as file:
          content = file.read()
          dic = json.loads(content, object_pairs_hook=collections.OrderedDict)
          # dic_all = json.dumps(dic, ensure_ascii=False)
          body_dic = (dic[id_str])
          group =[]
          group = body_dic.keys()
          l = 0
          for p in range(len(group)):
               value = list(body_dic.values())[p]
               if '_D' in list(group)[p]:
                    value_change10 = int('0x'+body_str[l:l+value], 16)
                    print(list(group)[p] + ': %s' % value_change10)
               elif '_B' in list(group)[p]:
                    # print(body_str[l:l+value])
                    value_change2 = bin(int('0x'+body_str[l:l+value], 16))
                    if (value_change2 == '0b0'):
                         value_change2 = '0'*value*4
                    else:
                         value_change2 = value_change2[2:]
                    value_change2 = (' '.join(re.compile('.{4}').findall(value_change2)))
                    print(list(group)[p] + ': %s' % value_change2)
               else:
                    print(list(group)[p] + ': ' + body_str[l:l+value])
               l = l+value

if __name__ == "__main__":
     # str = "7E 80 09 00 00 01 50 02 74 94 68 00 19 4B 7E"
     str = "7E 00 01 00 00 01 50 02 74 94 68 00 19 00 01 01 11 00 4B 7E"
     # str = "7E 80 05 00 10 01 50 02 74 94 68 00 01 00 01 02 58 00 02 01 02 03 04 05 06 00 03 0C 0D 7E"
     # str = "7e0200004044034343557112ce00000000000c000201ab7d6706e23f5b001b00000000190613122316010400005daa02020000030200002504000000002a0200022b0400010000300113310113247e"
     str = str.replace(' ', '')
     json_txt(str)
