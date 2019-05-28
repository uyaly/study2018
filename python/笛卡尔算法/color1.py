# coding:UTF-8
# 小明口袋有4个球，分别是红色，红色，黄色，蓝色。每次随机取出一个球记下颜色，然后再放回口袋，小明一共取了两次球，不考虑顺序，请给出所有颜色组合

b0 = ['r','r','y','b']
b1 = ['r','r','y','b']
b = ['r','r','y','b']

ball = ''
ball1 = ''
ballall = []    # 所有排列组合
ballresult = []  # 结果
for i in range(len(b0)):
    for j in range(len(b1)):
        if [b0[i], b1[j]] not in ballresult and [b1[j], b0[i]] not in ballresult:
            ballresult.append([b0[i], b1[j]])

# for i in range(len(b)-1):
#     # for j in range(len(b)):
#         if [b[i], b[i+1]] not in ballresult and [b[i+1], b[i]] not in ballresult:
#             ballresult.append([b[i], b[i+1]])

print(ballresult)
