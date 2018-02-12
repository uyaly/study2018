from jt808.tools import config
from jt808.tools import tools

import time

class GPSInfo:
    #从GPSinfo.txt 和Config.py中获取数据
    def __init__(self, GPSList):
        self.t = tools.Tools()
        self.setAlarmData(config.ALARM)
        self.setStateData(config.STATE)
        self.setLongitudeData(GPSList[1])
        self.setLatitudeData(GPSList[0])
        self.setElevationData(config.ELEVATION)
        self.setSpeedData(config.SPEED)
        self.setDirectData()
        self.setDateData()
        self.setMileageData(config.MILEAGE)
        # self.setOliData(Config.OIL)
        self.set_video_alarm_date(config.VIDEO_ALARM)

    def getData(self):
        self.data = (self.getAlarmData() +
                     self.getStateData() +
                     self.getLongitudeData() +
                     self.getLatitudeData() +
                     self.getElevationData() +
                     self.getSpeedData() +
                     self.getDirectData() +
                     self.getDateData() +
                     self.getMileageData() +
                     # self.getOliData() +
                     self.get_video_alarm_date()
                     )
        return self.data

    # 报警
    def getAlarmData(self):
        return self.alarmData

    def setAlarmData(self, tempInt):
        #指定报警
        # hexBinData = int(tempInt, 2)
        # self.alarmData = self.t.IntToHex(hexBinData, 8)

        #随机报警
        strBin = ''.join(tempInt)
        hexBinData = int(strBin,2)
        self.alarmData = self.t.IntToHex(hexBinData, 8)

    # 状态
    def getStateData(self):
        return self.stateData

    def setStateData(self, tempInt):
        strBin = ''.join(tempInt)
        hexBinData = int(strBin, 2)
        self.stateData = self.t.IntToHex(hexBinData, 8)

    # 经度
    def getLongitudeData(self):
        return self.lonData

    def setLongitudeData(self, tempDouble):
        lonNum = int(float(tempDouble) * 1000000)
        self.lonData = self.t.IntToHex(lonNum, 8)

    # 纬度
    def getLatitudeData(self):
        return self.latData

    def setLatitudeData(self, tempDouble):
        latNum = int(float(tempDouble) * 1000000)
        self.latData = self.t.IntToHex(latNum, 8)

    # 海拔
    def getElevationData(self):
        return self.eleData

    def setElevationData(self, tempInt):
        self.eleData = self.t.IntToHex(tempInt, 4)

    # 速度
    def getSpeedData(self):
        return self.speedData

    def setSpeedData(self, tempFloat):
        self.speedData = self.t.IntToHex(tempFloat, 4)

    # 方向
    def getDirectData(self):
        return self.dirData

    def setDirectData(self):
        self.dirData = "0020"

    # 时间
    def getDateData(self):
        return self.dateData

    def setDateData(self):
        self.dateData = time.strftime("%y%m%d%H%M%S", time.localtime())

    # 里程
    def getMileageData(self):
        return self.milData

    def setMileageData(self, tempInt):
        milNum = self.t.IntToHex(tempInt*10, 8)
        self.milData = '0104' + milNum

    # # 油量
    # def getOliData(self):
    #     return self.oilData
    #
    # def setOliData(self, tempInt):
    #     oilNum = self.t.IntToHex(tempInt, 2)
    #     self.oilData = '0202' + oilNum

    #视频报警
    def get_video_alarm_date(self):
        return self.video_alarm_Data
    def set_video_alarm_date(self,tempInt):
        #指定报警
        hexBinData = int(tempInt,2)
        self.video_alarm_Data = '1404' + self.t.IntToHex(hexBinData, 8)

if __name__ == '__main__':
    g = GPSInfo([116.710593,39.520727])
    print('GPS测试：',g.getData())
