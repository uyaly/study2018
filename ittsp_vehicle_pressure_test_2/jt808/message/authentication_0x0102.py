# coding:utf-8
# 鉴权

from jt808.tools import tools

class Authentication:
    def __init__(self):
        self.t = tools.Tools()
        self.autID = 'vmsgps'
        
    def setAut(self, aID='vmsgps'):
        self.autID = aID

    def getData(self):
        self.strHex = self.t.StrToHex(self.autID)
        return self.strHex


if __name__ == '__main__':
    a = Authentication()
    print('鉴权测试：',a.getData())