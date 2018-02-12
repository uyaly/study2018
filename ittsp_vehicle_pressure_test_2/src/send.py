# coding:utf-8
import time,os,sys
import traceback

CAR_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(CAR_PATH)
from jt808.tools import config
from src import body_data


class Send:
    # 建立Socket连接， 并且注册
    def __init__(self, sim, vID, dID, tcp):
        self.vID = vID
        self.dID = dID
        self.sim = sim
        self.tcp = tcp
        self.data = body_data.BodyData(sim)

        self.tcp.settimeout(30)

    # 发送注册
    def sendReg(self):
        reg =  self.data.register_0x0100(self.vID, self.dID)
        self.tcp.send(bytes.fromhex(reg))
        config.BYTES += len(bytes.fromhex(reg))
        print(self.tcp.getsockname(), self.vID + '上线了')
        self.failLog('注册', reg)

    # 发送鉴权
    def sendAut(self):
        aut = self.data.authentication_0x0102('vmsGPS')
        self.tcp.send(bytes.fromhex(aut))
        config.BYTES += len(bytes.fromhex(aut))
        self.failLog('鉴权', aut)

    # 发送GPS
    def sendGPS(self, GPSList):
        gps = self.data.gpsInfo_0x0200(GPSList)
        self.tcp.send(bytes.fromhex(gps))
        config.BYTES += len(bytes.fromhex(gps))
        #self.failLog('gps', gps)

    # 发送心跳
    def sendHeart(self):
        heart = self.data.heartbeat_0x0002()
        self.tcp.send(bytes.fromhex(heart))
        config.BYTES += len(bytes.fromhex(heart))
        #self.failLog('心跳', heart)

    # 记录错误日志
    def failLog(self, strData, send_data):
        try:
            self.tcp.recv(1024)
        except:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + self.vID + ' ' + self.sim + '\n')
            print(traceback.print_exc())
            config.FAIL += 1
            with open('log\\resAndaut_error.txt', 'a') as f:
                f.writelines(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + self.vID + "发送了" + strData + " >>> " + send_data + '\n' )
                f.writelines(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + self.vID + ' ' + self.sim + '\n')
                traceback.print_exc(file=f)
                f.flush()
