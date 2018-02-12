class JoinData:
    def __init__(self, sim):
        if 12 == len(sim):
            self.sim = sim
        else:
            self.sim = '0' + sim
    #完整拼报 = 消息头 + 内容包 + 尾部校验
    def getFullData(self, iID, bodyData):
        self.dataHead = self.setHead_Data(iID)
        self.dataBody = bodyData
        self.dataTail = self.setTail_Data(self.dataHead, self.dataBody)
        formatData = (self.dataHead + self.dataBody + self.dataTail).upper()[2:-2]
        formatData = formatData.replace('7D', '7D01')
        formatData = formatData.replace('7E', '7D02')
        fullData = '7E' + formatData + '7E'
        return fullData

    #设置消息头
    def setHead_Data(self, iID):
        self.info_Head = '7E'
        self.info_ID = iID
        self.info_Attribute = '002E'
        self.info_SIM = self.sim
        self.info_Serial = '0000'
        self.dataHead = self.info_Head + self.info_ID + self.info_Attribute + self.info_SIM + self.info_Serial
        return self.dataHead

    #设置消息尾
    def setTail_Data(self, dataHead, dataBody):
        self.calc = dataHead + dataBody
        self.code = self.checksum(self.calc)
        return self.code + '7E'
    
    #尾部计算校验
    def checksum(self, dataStr):
        res = 0
        index = 0
        list1 = []
        for each in bytes.fromhex(dataStr)[1:]:
            index += 1
            list1.append(each)

        for each in list1:
            # print('res = {}, each = {}'.format(res, each))
            if index == 0:
                res = each
            else:
                res = res ^ each

        res = hex(res)[2:]

        if 1 == len(res):
            res = '0' + res

        return res

