# coding:utf-8
import time,os,sys
import xlrd
from socket import *
CAR_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(CAR_PATH)
# from jt808.tools import config
# from src import send


class ThreadGPS:

    def __init__(self, file, ip, port):
        self.file = file
        self.ip = ip
        self.port = port

        self.socketInit()
        self.GPSList = self.getGPSList()

    def socketInit(self):
        try:
            tcp = socket(AF_INET, SOCK_STREAM)
            tcp.connect((self.ip, self.port))
            print('{}连接成功...'.format(tcp.getsockname()))
        except:
            print('无法连接！！！')
            return -1

        count = 0
        self.vehicleList = []
        try:
            table_send = xlrd.open_workbook(CAR_PATH + r'\car\test.xls').sheets()[0]
        except IOError:
            print('读取表错误!')
        for each in range(1,table_send.nrows):
            if count == 5:
                tcp = socket(AF_INET, SOCK_STREAM)
                tcp.connect((self.ip, self.port))
                count = 0

            sends = send.Send(table_send.row_values(each)[3], table_send.row_values(each)[1], table_send.row_values(each)[2], tcp)
            self.vehicleList.append(sends)
            count += 1
            if table_send.row_values(each)[1] == '' or table_send.row_values(each)[2] == '' or table_send.row_values(each)[3] == '':
                continue


    def getGPSList(self):
        GPSList = []
        try:
            table_gps = xlrd.open_workbook(CAR_PATH + r'\gps\test.xls').sheets()[0]
        except IOError:
            print('读取表错误!')
        for each in range(1,table_gps.nrows):
            if table_gps.row_values(each)[0] == '' or table_gps.row_values(each)[1] == '':
                continue
            GPSList.append([table_gps.row_values(each)[0],table_gps.row_values(each)[1]])
        print(GPSList)
        return GPSList

    def run(self):
        self.flag = True
        try:
            self.vehicleList
        except AttributeError:
            while self.socketInit() == -1:
                print('再次启动程序，玩命连接中...')
                if self.flag == False:
                    return

        for each in self.vehicleList:
            each.sendReg()
            each.sendAut()
            config.ONLINE += 1

            if self.flag == False:
                break

        gpsIndex = 0
        while self.flag:
            try:
                for each in self.vehicleList:
                    each.sendGPS(self.GPSList[gpsIndex])
                    config.GPS += 1
                    each.sendHeart()
                    config.HEART += 1

                # print(self.GPSList[gpsIndex])
                gpsIndex += 1
                if gpsIndex >= len(self.GPSList):
                    gpsIndex = 0
                time.sleep(5)
            except ConnectionAbortedError as e:
                print(e)
                print('正在尝试重新连接...')
                self.socketInit()


    def stop(self):
        self.flag = False
        print('# ----------- 停止程序 ----------- #')


if __name__ == '__main__':
    print(ThreadGPS.CAR_PATH)