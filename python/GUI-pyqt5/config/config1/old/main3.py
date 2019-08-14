# coding:UTF-8
import json
import collections
import re

def json_txt(str):
     str = str.replace(' ', '')
     if ((str[0:2] == '7e') and (str[-2:] == '7e')) or ((str[0:2] == '7E') and (str[-2:] == '7E')) :
          result = ("消息ID："+str[2:6])+ '\n'
          result += ("消息体长度："+str[6:10])+ '\n'
          result += ("终端ID："+str[10:22])+ '\n'
          result += ("消息流水号："+str[22:26])+ '\n'
          result += ("消息体："+str[26:-4])+ '\n'
          result += ("校验位："+str[-4:-2])+ '\n'
          result += ('-'*20)+ '\n'
          # print("________说明  _D:十进制,_B:二进制________")
          # print("标识符:"+str[0:2])
          # print("消息ID："+str[2:6])
          # print("消息体长度："+str[6:10])
          # print("终端ID："+str[10:22])
          # print("消息流水号："+str[22:26])
          # print("消息体："+str[26:-4])
          # print("校验位："+str[-4:-2])
          # # print("标识符:"+str[-2:])
          id_str = str[2:6]
          body_str = str[26:-4]
          # print('-'*10)

          with open('config.txt', 'r', encoding='utf-8') as file:
               content = file.read()
               dic = json.loads(content, object_pairs_hook=collections.OrderedDict)
               # dic_all = json.dumps(dic, ensure_ascii=False)
               if id_str in dic:
                    body_dic = (dic[id_str])
                    group = body_dic.keys()
                    l = 0
                    for p in range(len(group)):
                         value = list(body_dic.values())[p]
                         if '_D' in list(group)[p]:
                              value_change10 = int('0x'+body_str[l:l+value], 16)
                              print(list(group)[p] + ': %s' % value_change10)
                              result += (list(group)[p] + ': %s' % value_change10)+ '\n'
                         elif '_B' in list(group)[p]:
                              # print(body_str[l:l+value])
                              value_change2 = bin(int('0x'+body_str[l:l+value], 16))
                              if (value_change2 == '0b0'):
                                   value_change2 = '0'*value*4
                              else:
                                   value_change2 = value_change2[2:]
                              value_change2 = (' '.join(re.compile('.{4}').findall(value_change2)))
                              print(list(group)[p] + ': %s' % value_change2)
                              result += (list(group)[p] + ': %s' % value_change2)+ '\n'

                         else:
                              print(list(group)[p] + ': ' + body_str[l:l+value])
                              result += (list(group)[p] + ': ' + body_str[l:l+value])+ '\n'
                         l = l+value
               else:
                    result = "请先配置，再分析"

     else :
          result = "内容不合法"
     return result
     # print(result)

if __name__ == "__main__":
     # str = "7E 80 09 00 00 01 50 02 74 94 68 00 19 4B 7E"
     # str = "7E 00 01 00 00 01 50 02 74 94 68 00 19 00 01 01 11 00 4B 7E"
     # str = "7E 80 05 00 10 01 50 02 74 94 68 00 01 00 01 02 58 00 02 01 02 03 04 05 06 00 07e0200004044034343557112ce00000000000c000201ab7d6706e23f5b001b00000000190613122316010400005daa02020000030200002504000000002a0200022b0400010000300113310113247e3 0C 0D 7E"
     str = ""
     str = str.replace(' ', '')
     json_txt(str)
