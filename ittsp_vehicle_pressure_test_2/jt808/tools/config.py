# coding:utf-8
import multiprocessing
import time
import random


# -----------基础信息----------- #
# SIM
SIM_INFO = '018988888888'
# 终端ID
D_ID = '8888888'
# 车牌号
V_ID = '测C88888'
# 车辆颜色ID
COLOR = '02'
# 省域ID
PROVINCE = '007B'
# 市域ID
CITY = '007B'
# 制造商ID
MAKER = '12345'
# 终端型号
DEVICEMODEL = 'A123456'



# -----------GPS信息----------- #
# 指定报警
ALARM = ['0' for x in range(32)]
print(ALARM)
# def alarm():
#     ALARM = ''
#     for i in range(32):
#         if i == 31:
#             add = 1
#         else:
#             add = 0
#         ALARM += str(add)
#     return ALARM
# ALARM = alarm()

#随机报警
# ALARM = [str(random.randint(0,1)) for x in range(32)]
if __name__ == '__main__':
    print(ALARM)
# 状态
STATE = [str(random.randint(0,1)) for x in range(32)]
# 海拔
ELEVATION = 802
# 速度
SPEED = 67

# 附加信息
# 里程
MILEAGE = 2000
# 油量
OIL = 100
# 视频报警
def alarm1():
    ALARM = ''
    for i in range(32):
        if i == 31:
            add = 1
        else:
            add = 0
        ALARM += str(add)
    return ALARM
VIDEO_ALARM = alarm1()

# -----------GUI信息----------- #
START_TIME = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# -----------多进程信息----------- #
gps_count = multiprocessing.Value('L', 0)
hear_count = multiprocessing.Value('L', 0)
online_car = multiprocessing.Value('L', 0)
bytes_count = multiprocessing.Value('L', 0)
send_fail = multiprocessing.Value('L', 0)

# -----------多线程信息----------- #
GPS = 0
HEART = 0
ONLINE = 0
BYTES = 0
FAIL = 0
