# coding:utf-8
from jt808.tools import config
from jt808.tools import tools

#终端注册

class Register:
    def __init__(self, vID, dID):
        self.t = tools.Tools()
        self.setvIDData(vID)
        self.setdIDData(dID)
        self.setColorData(config.COLOR)
        self.setProvinceData(config.PROVINCE)
        self.setCityData(config.CITY)
        self.setMakerData(config.MAKER)
        self.setDeviceModel(config.DEVICEMODEL)

    def getData(self):
        self.data = (
                     self.getProvinceData() +
                     self.getCityData() +
                     self.getMakerData() +
                     self.getDeviceModel() +
                     self.getdIDData() +
                     self.getColorData() +
                     self.getvIDData()
                     )
        return self.data

    # 终端ID
    def getdIDData(self):
        return self.dIDData

    def setdIDData(self, tempStr):
        dIDNum = self.t.StrToHex(tempStr)
        if 14 != len(dIDNum):
            dIDNum = dIDNum + ((14-len(dIDNum))*'0')
        self.dIDData = dIDNum

    # 车牌号
    def getvIDData(self):
        return self.vIDData

    def setvIDData(self, tempStr):
        vIDNum = self.t.ChrToHex(tempStr[0])
        vIDNum = vIDNum + self.t.StrToHex(tempStr[1:])
        if 18 != len(vIDNum):
            vIDNum = vIDNum + ((18-len(vIDNum))*'0')
        self.vIDData = vIDNum

    # 车牌颜色
    def getColorData(self):
        return self.coloData

    def setColorData(self, tempHex):
        self.coloData = tempHex

    # 省域ID
    def getProvinceData(self):
        return self.provinceData

    def setProvinceData(self, tempHex):
        self.provinceData = tempHex

    # 市域ID
    def getCityData(self):
        return self.CityData

    def setCityData(self, tempHex):
        self.CityData = tempHex

    # 制造商
    def getMakerData(self):
        return self.makerData

    def setMakerData(self, tempChr):
        self.makerData = self.t.StrToHex(tempChr)

    # 终端型号
    def getDeviceModel(self):
        return self.dmData

    def setDeviceModel(self, tempChr):
        sHex = self.t.StrToHex(tempChr)
        if 40 != len(sHex):
            self.dmData = sHex + ((40-len(sHex))*'0')

if __name__ == '__main__':
    a = Register('鄂A00001','OO00001')
    print('终端注册测试：',a.getData())
