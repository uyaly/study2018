# coding:utf-8
import pytest
import requests
import urllib3
#使用这个方法就看不到警告
urllib3.disable_warnings()

url = "https://rongwei.rtisp.cn:14009"
url1 = "https://192.168.3.183:14009"
# access_token1 = "3dcabfce-7fd7-4b27-8a87-02f1134026aa"
chipId = "596051"
alarmId = "128"
telephone = "13800000007"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    }

def test_s1(login):
    # querystring = {
    #         "id":chipId,
    #         # "type":"2",
    #         "access_token":access_token
    #        }
    # carriers = requests.request("GET", url1 + "/user/carriers/details", headers=headers, params=querystring)
    print(u"3.获取芯片载体信息详情:")
    # print(carriers.text)
def test_s2():  # 不传login
    print("用例2：不需要登录，操作222")
def test_s3(login):
    print("用例3：登录之后其它动作333")

if __name__ == "__main__":
    pytest.main(["-s", "test_fixt1.py"])