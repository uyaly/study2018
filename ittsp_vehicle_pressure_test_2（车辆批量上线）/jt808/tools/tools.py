# coding:utf-8
import binascii

class Tools:

    # 字符串转16进制
    def StrToHex(self, tempStr):
        s = ''
        for each in tempStr:
            s += hex(ord(each))[2:]
        return s.upper()

    # 16进制转8位的2进制
    def HexStrTo8Bin1(self, tempHex):
        res = ''
        for each in bytes.fromhex(tempHex):
            sBin = bin(each)[2:]
            eightNum = 8 - len(sBin)
            if(0 != eightNum):
                sBin = eightNum * '0' + sBin
            res += sBin
        return res

    # 整形转16进制，缺位补0
    def IntToHex(self, tempInt, digit):
        sHex = hex(tempInt)[2:]
        num = digit - len(sHex)
        if(0 != num):
            sHex = num * '0' + sHex
        return sHex

    # 中文转16进制
    def ChrToHex(self, tempChr):
        sHex = str(binascii.b2a_hex(tempChr.encode('gbk')))[2:-1].upper()
        return sHex

    #bytes转16进制
    def ByteToHex(self, bins):
        return ''.join(["%02X" % x for x in bins]).strip()



# print(bytes(b'~\x81\x00\x00\t\x01Rpa\x11\x11$c\x00\x01\x00vmsgps\x80~').decode('ascii'))

