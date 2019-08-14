# coding:UTF-8
import re

# 消息体
str = '000000000000000006D2209B01D15CC100000000000019070510470000000000000000000000000000000000000000000000000000000000000000000000'
# str.split(' ')
str1 = str.replace(' ', '')
strnew = (' '.join(re.compile('.{2}').findall(str)))

temp = strnew.replace(' ', ',')
strlist = temp.split(',')
yihuo = 0
for i in strlist:
    yihuo = int('0x'+i, 16) ^ yihuo
print(str1)
print(strnew)
print("消息体长度:{0}字节 = {1}".format(len(strlist),hex(len(strlist))))
print("消息体异或:{0}".format(hex(yihuo)))
# 0009 003E 013000000000 0001