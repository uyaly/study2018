import json
import requests
import xlrd
import datetime
from xlutils.copy import copy

def vms_login_session():
    """
    获取用户登录cookies
    :return:
    """
    seesion = requests.session()
    vms_login_url = "http://59.172.105.83:81/vmsBS/monitor/login.do"
    data = {"username": "system", "password": "ycig008@123", "orgCode": "B"}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    r = seesion.post(url=vms_login_url, data=data, headers=headers)
    cookies = requests.utils.dict_from_cookiejar(seesion.cookies)
    return cookies

def vms_v_sum(index):
    """
    获取组织树数据
    :param index: 传入的标签页面所有，在线，行驶
    :return:
    """
    url = "http://59.172.105.83:81/vmsBS/monitor/getdefaultmonitor.do"
    data = {"treeStatus": index}
    headers = {'X-Requested-With': 'XMLHttpRequest'}
    try:
        resp = requests.post(url=url, headers=headers, cookies=vms_login_session(), data=data, timeout=3)
        return resp.json()
    except Exception as err:
        return err

def vms_v_sums(index):
    """
    获取组织树二级节点数据
    :param index: 传入的标签页面所有，在线，行驶
    :return:
    """
    url = "http://59.172.105.83:81/vmsBS/monitor/getdefaultmonitor.do"
    data = {"treeStatus": index, "groupischecked": "false"}
    payload = {'id':'B'}
    headers = {'X-Requested-With': 'XMLHttpRequest'}
    try:
        resp = requests.post(url=url,cookies=vms_login_session(), data=payload, headers=headers, params=data, timeout=3)
        return resp.json()
    except Exception as err:
        return err

def record_xls():
    """
    实时数据追加到xls（Sheet1），读取参数（Sheet2）
    :return: 要发送的文本，即在线总数低于参数的单位和实时数据
    """
    data = xlrd.open_workbook(r'E:\PycharmProjects\test\study\python\车联网车辆树在线车辆监控\统计.xls')
    # data = xlrd.open_workbook(r'统计.xls')
    table = data.sheet_by_name(u'Sheet1')
    table2 = data.sheet_by_name(u'Sheet2')
    row_n = table.nrows
    col_n = table2.ncols
    newWb = copy(data)
    newWs = newWb.get_sheet(0)
    now_time = datetime.datetime.now()
    # hour_str = datetime.datetime.strftime(now_time, '%H')
    time_str = datetime.datetime.strftime(now_time, '%Y-%m-%d %H:%M:%S')
    list = get_data()
    hour = now_time.hour
    col = 0
    for k in range(1,col_n-1):
        if(hour >= int(table2.cell(0,k).value) and hour < int(table2.cell(0,k+1).value)):
            col = k
    msg = ''
    for j in range(len(list)):
        newWs.write(row_n+j, 0, list[j][0])   # 单位名
        newWs.write(row_n+j, 1, list[j][1])   # 所有
        newWs.write(row_n+j, 2, list[j][2])   # 在线
        newWs.write(row_n+j, 3, list[j][3])   # 行驶
        newWs.write(row_n+j, 4, hour)   # 时间
        newWs.write(row_n+j, 5, time_str)   # 日期
        if ((list[j][2]) < int(table2.cell(j+1,col).value)):
            msg += "【%s】| 所有：%d | 在线：%d | 行驶：%d  \n" %(list[j][0],list[j][1],list[j][2],list[j][3])
    newWb.save(r'E:\PycharmProjects\test\study\python\车联网车辆树在线车辆监控\统计.xls'); # 保存
    # newWb.save(r'统计.xls'); # 保存
    if msg == '':
        msg = '一切正常'
    # print(msg)
    return msg

def get_data():
    # 获取全部值
    num_list = []
    allname = []
    allname.append(vms_v_sum(0)[0]["text"])
    for i in range(0,3):
        allname.append(vms_v_sum(i)[0]["attributes"]["total"])
    num_list.append(allname)
    # 获取各子项值
    for m in range(9):
        childname = []
        childname.append(vms_v_sums(0)[m]["text"])
        for n in range(0,3):
            childname.append(vms_v_sums(n)[m]["attributes"]["total"])
        num_list.append(childname)
    return num_list

def send_msg(api_token, title, text):
    """
    钉钉机器人接口
    msgtype	true	string	此消息类型为固定markdown
    title	true	string	首屏会话透出的展示内容
    text	true	string	markdown格式的消息
    atMobiles	Array	否	被@人的手机号(在text内容里要有@手机号)
    isAtAll	bool	否	@所有人时：true，否则为：false
    :param text:
    :return:
    """
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    json_text = {
        "msgtype": "markdown",
        "markdown": {
            "title": title,
            "text": "## **%s**\n" % title +
                    "> %s\n" % text
        },
        "at": {
            "atMobiles": ["xxxxxxx"],
            "isAtAll": False
        }
    }
    requests.post(api_token, json.dumps(json_text), headers=headers).json()

if __name__ == '__main__':
    # 格式化输出文本
    str = record_xls()
    # 调用钉钉机器人发信息
    send_msg("https://oapi.dingtalk.com/robot/send?access_token=cbe3017d8e307959e73b9886f48059f1a1ec23026caac816727c57a17286e00f",
           "车联网综合信息服务平台", str)
