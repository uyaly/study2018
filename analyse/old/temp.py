
# str1 = '40'
# str2 = '85'
# num1 = int(str1, 16)
# num2 = int(str2, 16)
#
# ss = ((hex(num1 ^ num2))[2:])
# print(type(ss))
# print(ss)
from tool import apart_str,exchange_D_H,exchange_D_B,exchange_B_H
str = " 80 00 00 00 00 10 13 06 CE F9 C0 01 D1 D6 24 00 00 00 00 00 00 19 08 23 10 55 28 01 04 00 01 2F 50 02 02 00 00 03 02 00 00 31 01 00 14 04 00 00 00 00 30 01 36 F0 01 03 F1 0A 30 8C AC 53 24 4F 18 00 74 8C F2 01 00 F3 02 03 63 F4 04 00 07 F1 FF E1 01 8B EC"
str = str.replace(' ', '')
str_len = len(apart_str(str, 2))-1  # 消息体包数
num = "{0:>010s}".format(exchange_D_B(str_len)[2:])  # 消息体包数转二进制，不足10位补0
str = '10000' + (num)   # 合并“消息体属性”
q = exchange_B_H(str)  # 转16进制
print(q)
