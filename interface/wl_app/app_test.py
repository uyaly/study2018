# coding:utf-8
import requests
url = "http://192.168.3.54:14010/iot/login.do"

access_token1 = "3dcabfce-7fd7-4b27-8a87-02f1134026aa"
chipId = "596051"
alarmId = "128"
telephone = "13800000007"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    }

# payload = {"password":"000000",
#            "username":"13800000007",
#            "grant_type":"password",
#            "scope":"app",
#            "client_secret":"secret",
#            "client_id":"client",
#            }
# login = requests.request("POST", url + "/oauth/token", data=payload, headers=headers)
# print(u"1.登录验证:")
# print(login.text)
#
# querystring = {
#             "id":chipId,
#             # "type":"2",
#             "access_token":access_token1
#            }
# carriers = requests.request("GET", url1 + "/user/carriers/details", headers=headers, params=querystring)
# print(u"3.获取芯片载体信息详情:")
# print(carriers.text)

payload = {
            "chipId":chipId,
            "startTime":"2018-02-10",
            "endTime":"2018-02-13",
            "access_token":access_token1
           }
defence_set = requests.request("post", url1 + "/defence/set", data=payload, headers=headers)
print(u"4.设防:")
print(defence_set.text)


# payload = {
#             "chipId":chipId,
#             "access_token":access_token1
#            }
# defence_revoke = requests.request("post", url1 + "/defence/revoke", data=payload, headers=headers)
# print(u"5.撤防:")
# print(defence_revoke.text)

# payload = {
#             "chipId":chipId,
#             "address":2,
#             "access_token":access_token1
#            }
# alarm_add = requests.request("post", url1 + "/alarm/add", data=payload, headers=headers)
# print(u"6.一键报警:")
# print(alarm_add.text)

# payload = {
#             "alarmId":alarmId,
#             "access_token":access_token1
#            }
# alarm_revoke = requests.request("post", url1 + "/alarm/revoke", data=payload, headers=headers)
# print(u"7.撤销报警:")
# print(alarm_revoke.text)

# payload = {
#             "alarmId":alarmId,
#             "access_token":access_token1
#            }
# alarm_confirm = requests.request("post", url1 + "/alarm/confirm", data=payload, headers=headers)
# print(u"8.确认报警:")
# print(alarm_confirm.text)


# payload = {
#             "id":chipId,
#             "trace_date":"2017-02-12",
#             "access_token":access_token1
#            }
# traces = requests.request("post", url1 + "/user/carriers/traces", data=payload, headers=headers)
# print(u"9.历史足迹:")
# print(traces.text)


# payload = {
#             "id":chipId,
#             "access_token":access_token1,
#             "type" : "2",
#            }
# alarmRecord = requests.request("post", url1 + "/user/carriers/alarmRecord", data=payload, headers=headers)
# print(u"10.报警记录:")
# print(alarmRecord.text)

# payload = {
#             "telephone":telephone,
#             "access_token":access_token1,
#            }
# oldman = requests.request("post", url1 + "/base/oldman/list", data=payload, headers=headers)
# print(u"11.我家老人:")
# print(oldman.text)

# payload = {
#             "telephone":telephone,
#             "access_token":access_token1,
#            }
# pet = requests.request("post", url1 + "/base/pet/list", data=payload, headers=headers)
# print(u"12.我的宠物:")
# print(pet.text)


# payload = {
#             "telephone":telephone,
#             "access_token":access_token1,
#            }
# vehicle = requests.request("post", url1 + "/base/vehicle/list", data=payload, headers=headers)
# print(u"13.我的电动车:")
# print(vehicle.text)