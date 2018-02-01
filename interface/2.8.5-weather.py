# coding:utf-8
import requests
import json
import time
url = "http://www.weather.com.cn/weather/101200101.shtml"
headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0" }
# get方法加个ser-Agent就可以了
s = requests.session()
r = s.get(url, headers=headers, verify=False)
print r.content

# print r.apparent_encoding
# time.sleep(10)
# result = r.json()
# data = result["23d"]
# print data[0]