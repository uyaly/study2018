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
    try:
        id = response.json()["pois"][0]["id"]
        # print(response.json())
        # print(id)
        return (id)
    except:
        print(keyword+":id未找到")

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
            # print(keyword_name+" "+keyword_shape)
            newWs.write(row_n + j, 0, group)  # 组名
            newWs.write(row_n + j, 1, keyword_name)  # 关键字
            newWs.write(row_n + j, 2, keyword_shape)  # 边界
        except:
            newWs.write(row_n + j, 0, group)  # 组名
            newWs.write(row_n + j, 1, keyword_name)  # 关键字
            print(keyword_name+ "  未找到")
        j += 1


    newWb.save(r'data.xls'); # 保存

if __name__ == '__main__':
    group = "光谷八小"
    keywords = ["瑞成雅居","祥和雅居","成园","蓝光公寓","关东公寓","森林花园","新嘉园","新世界恒大华府","恒大华府","葛洲坝世纪花园","万科·嘉园","406 库宿舍","缝纫机厂宿舍","微型电机厂宿舍","康居园","文华学院教工公寓","体育职业学院教工宿舍","士官学校宿舍"]
    record_xls(group, keywords)

    # 1 d
    # "关山春晓", "金地太阳城", "逸景华庭", "江城雅居", "融科天域", "光谷新世界", "长航蓝晶国际", "阁调小区", "丽岛漫城", "保利时代", "保利时代天悦", "宏祥花园", "武职教工宿舍"
    # 1 x
    # "洪福家园", "洪福添美", "枫林上城", "金地阳光城", "阳光在线", "曙光嘉园", "关山还建小区（鲁广花园", "中杰阳光", "阳光尚东）", "光谷汇景", "万科锦程", "曙光星城 A 区", "曙光星城 B 区", "光谷青年城", "美庐郡园", "金地格林东郡", "民大教工宿舍", "纺大教工宿舍"
    # 2
    # "万科城市花园", "万科红郡", "当代国际花园", "现代森林小镇"
    # 3
    # "流芳老街", "佛祖岭 A 区", "佛祖岭 B 区", "佛祖岭 C 区", "佛祖岭 E区", "佛祖岭 F 区"
    # 4
    # "光谷 one39", "光谷 8 号", "联投喻园", "金鑫国际", "汇博苑", "金梭花园", "金地华公馆", "学府佳园", "巴黎豪庭", "保利花园", "茉莉公馆", "东湖广场", "剑桥春天", "华中科技大学（东校区", "东一区", "东二区", "东三区", "喻园小区一期", "喻园小区二期", "高层小区）", "长飞社区", "鼓风机厂宿舍", "华乐花园", "黄家店", "华城花园", "虹景花园", "电信小区
    # 5
    # "南湖还建小区", "锦绣龙城", "中谷苑", "光谷苑", "梅花坞", "宝业丽都", "水蓝郡", "南波湾", "光谷自由城", "锦绣良缘", "津发小区", "清水源", "长城别苑", "立信公寓", "南湖时尚城", "政院小区", "中南财大教工宿舍
    # 6
    # "长城坐标城", "蓝域拿铁公寓", "芭比伦堡", "万科城花璟苑", "铁箕山社区", "光谷理想城", "汤逊湖社区", "香山美树", "光谷麒麟社", "关南小区（建发社区", "中建三局三公司）", "中建康城", "曙光二村", "中铁七局公租房", "华夏学院教工公寓"
    # 7
    # "达尚城", "大邱社区", "旭辉御府", "佛祖岭社区 D1 区", "佛祖岭社区 D2 区", "新特工业园宿舍", "富士康宿舍", "中芯国际宿舍", "联想宿舍", "商贸学院教工公寓"
    # 8
    # "蓝光 COCO", "荷叶山还建小区", "瑞成雅居", "祥和雅居", "成园", "蓝光公寓", "关东公寓", "森林花园", "新嘉园", "新世界恒大华府", "恒大华府", "葛洲坝世纪花园", "万科嘉园", "406 库宿舍", "缝纫机厂宿舍", "微型电机厂宿舍", "康居园", "文华学院教工公寓", "体育职业学院教工宿舍", "士官学校宿舍"
    # 9
    # "佳源花都", "光谷上城", "湖口社区", "迎宾家园", "天成美雅", "葛光小区", "陆景苑", "宇峰家园", "梓洲花苑", "天慧神秘墅", "二师院教工宿舍"
    # 10
    # "曙光星城 C 区", "江南家园", "谓语城", "山水华庭", "云顶居", "东林外庐", "清江山水 1-3 期"
    # 11
    # "洪福家园", "洪福添美", "枫林上城业主子女入学。保利蓝海郡", "南湖锦园", "金地中心城", "金地雄楚一号", "金地天悦", "八一花园", "南湖康泰花园", "柳林雅居", "柒零社区", "惠安新苑", "刘家咀村", "南湖锦城", "中博南湖康城"
    # 12
    # "天成美景", "城市之光", "宜盛花园", "金谷明珠园", "关南还建小区", "谷方社区", "光谷悦城"
    # 15
    # "鹏翔花园", "光谷平安春天", "当代国际城", "佛奥俊贤雅居", "金地艺境", "谷尚居", "万科魅力之城", "交通学校教工公寓"
    # 16
    # "驿山高尔夫", "国采光立方", "中建光谷之星", "山水年华（龙山郡）", "桃花源", "未来城公寓"
    # 17
    # "德欣里社区", "景源里社区", "三星苑社区", "明畅里社区", "清和里社区", "同安里社区", "九峰村", "九峰新区", "新跃村", "生物城人才公寓"
    # 18
    # "梅园社区", "橘园社区", "竹园社区", "兰园社区（含兰园", "桂园）", "棠园社区（含棠园", "槿园", "樱园）", "杏园社区（含杏园", "李园", "桃园）", "花山社区（集镇）", "未拆迁村湾"
    # 26
    # "碧桂园生态城", "亿达云山湖"
    # 27
    # "联投花山郡", "万科紫悦湾"

