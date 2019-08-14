# coding:utf-8
import os,sys
CAR_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(CAR_PATH)
from jt808.message import gpsInfo_0x0200
from jt808.message import join_data
from jt808.message import register_0x0100
from jt808.message import authentication_0x0102


class BodyData:
    def __init__(self, sim):
        self.joinData = join_data.JoinData(sim)
        self.fullData = ''

    # 注册
    def register_0x0100(self, vID, dID):
        self.reg = register_0x0100.Register(vID, dID)
        self.fullData = self.joinData.getFullData('0100', self.reg.getData())
        return self.fullData

    # 鉴权
    def authentication_0x0102(self, aID):
        self.aut = authentication_0x0102.Authentication()
        self.aut.setAut(aID)
        self.fullData = self.joinData.getFullData('0102', self.aut.getData())
        return self.fullData

    # 心跳
    def heartbeat_0x0002(self):
        self.fullData = self.joinData.getFullData('0002', '')
        return self.fullData

    # gps
    def gpsInfo_0x0200(self, GPSList):
        self.gps = gpsInfo_0x0200.GPSInfo(GPSList)
        print(GPSList)
        self.fullData = self.joinData.getFullData('0200', self.gps.getData())
        return self.fullData

