# coding:UTF-8
# 小明口袋有4个球，分别是红色，红色，黄色，蓝色。每次随机取出一个球记下颜色，然后再放回口袋，小明一共取了两次球，不考虑顺序，请给出所有颜色组合

from itertools import product
s = []
for x,y in product(['r','r','y','b'],['r','r','y','b']):
    # print(x,y)
    if [x,y] not in s and [y,x] not in s:
        s.append([x,y])

print(s)