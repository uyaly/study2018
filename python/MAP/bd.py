import requests
import json
import xlrd
import datetime
from xlutils.copy import copy

key = "0bec6cb86212adea871ef265712b00c5"


# response = requests.request("get", 'https://restapi.amap.com/v3/place/text?key=0bec6cb86212adea871ef265712b00c5&citylimit=true&output=json&keywords=保利花园&city=武汉')
# print(response.text)

def keyword_id(keyword, city):
    '''
    :param keyword: 关键字
    :param city: 城市
    :return: 关键字的id
    '''
    url = "https://restapi.amap.com/v3/place/text"
    querystring = {"key":key,"citylimit":"true","output":"json","keywords":keyword,"city":city}
    response = requests.request("get", url, params=querystring)
    id = response.json()["pois"][0]["id"]
    # print(response.json())
    # print(id)
    return(id)

def id_xy(id):
    '''

    :param id: 关键字id
    :return: 区域边界
    '''
    url = "https://ditu.amap.com/detail/get/detail"
    querystring = {"id":id}
    response = requests.request("get", url, params=querystring)
    # print(response.text)
    return(response.json())

def record_xls(group, keywords):
    '''
    将关键字的区域边界，写入xls
    :param keywords: 关键字数组
    :return:
    '''
    data = xlrd.open_workbook(r'data.xls')
    table = data.sheet_by_name(u'Sheet1')
    row_n = table.nrows
    newWb = copy(data)
    newWs = newWb.get_sheet(0)
    # now_time = datetime.datetime.now()
    # hour = now_time.hour
    j = 0
    for k in keywords:
        json_text = id_xy(keyword_id(k, "武汉"))
        # print(json_text)

        try:
            keyword_name = json_text["data"]["base"]["name"]
            keyword_shape = str(json_text["data"]["spec"]["mining_shape"]["shape"])
            newWs.write(row_n + j, 0, group)  # 组名
            newWs.write(row_n + j, 1, keyword_name)  # 关键字
            newWs.write(row_n + j, 2, keyword_shape)  # 边界
        except:
            newWs.write(row_n + j, 0, group)  # 组名
            newWs.write(row_n + j, 1, keyword_name)  # 关键字
            print(keyword_name+ "未找到")
        j += 1


    newWb.save(r'data.xls'); # 保存

if __name__ == '__main__':
    group = "光谷八小"
    keywords = ["蓝光 COCO","荷叶山小区","瑞成雅居","祥和雅居","成园","蓝光公寓","关东公寓","森林花园","新嘉园","新世界恒大华府","恒大华府","葛洲坝世纪花园","万科嘉园","406 库宿舍","缝纫机厂宿舍","微型电机厂宿舍","康居园","文华学院教工公寓","体育职业学院教工宿舍","士官学校宿舍"]
    record_xls(group, keywords)