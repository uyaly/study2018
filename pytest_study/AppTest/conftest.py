# coding:UTF-8
import pytest
import requests
import urllib3
import json
# 不带参数时默认scope="function"

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

payload = {"password":"000000",
           "username":"18062427385",
           "grant_type":"password",
           "scope":"app",
           "client_secret":"secret",
           "client_id":"client",
           }
@pytest.fixture()
def login():
    login = requests.request("POST", url1 + "/oauth/token", verify=False, data=payload, headers=headers)
    print(u"1.登录验证:")
    print(login.text)
    print(json.loads(login)['access_token'])
    return json.loads(login)['access_token']
