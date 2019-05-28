# coding:UTF-8
# 小明口袋有4个球，分别是红色，红色，黄色，蓝色。每次随机取出一个球记下颜色，然后再放回口袋，小明一共取了两次球，不考虑顺序，请给出所有颜色组合

import random

balls = ['r','r','y','b']
# balls = ['红色','红色','黄色','蓝色']
b = []
ball = ''
ball1 = ''
ballall = []    # 所有排列组合
ballresult = []  # 结果
for j in range(0, 100):
    b0 = random.choice(balls)
    b1 = random.choice(balls)
    ball = b0 + '&' + b1
    ball1 = b1 + '&' + b0
    if ball1 not in (ballall):
        ballall.append(ball1)
    # print(ballall)
    if (ball == ball1) and  ball not in(ballresult):
         ballresult.append(ball)

    elif ball not in (ballall) and ball not in(ballresult):
         ballresult.append(ball)

print(ballresult)
