# coding:UTF-8
import json
import collections
import re
from tool import exchange_B_D,exchange_H_B,exchange_H_D,exchange_bits,apart_str,exchange_D_H,exchange_D_B,exchange_B_H
class analyse():
    def apart_head(str):
        '''
        消息头拆分
        :param str: 消息头字符串
        :return: 拆分后的列表
        '''
        result = []
        result_bit = []
        # print(str)
        # print(str[32:36])
        result.append(["头-消息ID",str[:4]])
        result.append(["头-消息体属性" ,str[4:8]])
        # str1 = exchange_H_B(str[4:8])
        # result_bit.append(["头-消息体属性_版本标识", str1[1:2]])
        # result_bit.append(["头-消息体属性_分包", str1[2:3]])
        # result_bit.append(["头-消息体属性_加密方式", str1[3:6]])
        # result_bit.append(["头-消息体属性_消息体长度_D", exchange_B_D(str1[6:])])
        result.append(["头-协议版本号" ,str[8:10]])
        result.append(["头-终端手机号" ,str[10:30]])
        result.append(["头-消息流水号" ,str[30:34]])
        return result

    def join_head(list):
        '''
        消息头合并
        :param list:
        :return:
        '''
        result = ''
        for i in range(len(list)):
            result += list[i]
        return result

    def apart_body(body_str, body_dic):
        result = []
        keylist_dic = body_dic.keys()
        # print(keylist_dic)
        valuelist_dic = list(body_dic.values())
        l = 0
        for p in range(len(keylist_dic)):
            key = list(keylist_dic)[p]
            value = list(valuelist_dic)[p]
            if isinstance(value, dict): #判断value是否是字典类型isinstance 返回True false
                pass
            elif value == 0:
                result.append([key, body_str[l:]])
            else:
                result.append([key, body_str[l:l+value]])
                l = l + value
        return result

    def join_body(list):
        result = ''
        for i in range(len(list)):
            result += list[i]
        # print(result)
        return result

    def join_headattr(str_body):

        bodystr_len = len(apart_str(str_body, 2)) - 1  # 字符串消息体包数
        # bodystr_len = len(body_list)  # list消息体包数
        num = "{0:>010s}".format(exchange_D_B(bodystr_len)[2:])  # 消息体包数转二进制，不足10位补0
        str = '10000' + (num)  # 合并“消息体属性”
        # 1 0 000 0001010101 -->  1版本 0不分包 000不加密 ,消息体长度
        q = exchange_B_H(str)  # 转16进制
        return (q)

if __name__ == "__main__":
    #  消息头
    # str = "020040550100000000013800004444004E"
    # print(apart_head(str))
    list = [['头-消息ID：', '0200'], ['头-消息体属性：', '4055'], ['头-协议版本号：', '01'], ['头-终端手机号：', '00000000013800004444'], ['头-消息流水号：', '004E']]
    list = [[['头-消息ID：', '0200'], ['头-消息体属性：', '4055'], ['头-协议版本号：', '01'], ['头-终端手机号：', '00000000013800004444'], ['头-消息流水号：', '004E']],
            [['头-消息体属性_版本标识', '1'], ['头-消息体属性_分包', '0'], ['头-消息体属性_加密方式', '000'], ['头-消息体属性_消息体长度_D', '85']]]
    # print(join_head(list))
    # 消息体
    # str = "008000000000101306CEF9C001D1D624000000000000190823105528010400012F500202000003020000310100140400000000300136F00103F10A308CAC53244F1800748CF20100F3020363F4040007F1FFE1018B"
    # dic = OrderedDict([('报警标志_B', 8), ('报警标志', OrderedDict([('0', '紧急报警'), ('1', '超速报警'), ('2', '疲劳驾驶'), ('3', '危险预警'), ('4', 'GNSS 模块发生故障'), ('5', 'GNSS 天线未接或被剪断'), ('6', 'GNSS 天线短路'), ('7', '终端主电源欠压'), ('8', '终端主电源掉电'), ('11', '摄像头故障'), ('13', '超速预警'), ('14', '疲劳驾驶预警'), ('18', '当天累计驾驶超时报警'), ('19', '超时停车报警'), ('20', '进出区域报警'), ('21', '进出线路报警'), ('22', '路段行驶时间不足/过长报警'), ('23', '线路偏离报警')])), ('状态_B', 8), ('状态', OrderedDict([('0', '0 ACC关；1 ACC开'), ('1', '0 未定位；1 定位'), ('2', '0 北纬；1 南纬'), ('3', '0 东经；1 西经'), ('4', '0 运营；1 停运'), ('7', '1 车道偏移预警')])), ('纬度_D', 8), ('经度_D', 8), ('高程_D', 4), ('速度_D', 4), ('方向_D', 4), ('时间', 12)])
    # str = "7E 80 04 00 10 01 50 02 74 94 68 00 01 12 01 00 0D 7E"
    # apart_body(str,)
    str = ['0200', '4055', '01', '00000000013801804279', '004E', '00000000', '00001011', '00000000', '00000000', '0000', '0000', '0000', '190823105528', '010400012F500202000003020000310100140400000000300136F00103F10A308CAC53244F1800748CF20100F3020363F4040007F1FFE1018B']
    join_body(str)