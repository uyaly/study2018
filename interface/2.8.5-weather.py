# coding:utf-8
import requests
import json
import re
url = "http://www.weather.com.cn/weather/101200101.shtml"
headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0" }
# get方法加个ser-Agent就可以了
s = requests.session()
r = s.get(url, headers=headers, verify=False)
html = r.content

# 使用正则表达式模块re来查找返回内容中匹配的json格式数据，返回一个列表
res = re.search(r"\{\"(.*):([^\[]*)};", html)

print(res.group())

# 多了一个；号要去掉，使用字符串截取
str_json = res.group()[:-1]

# 字符串转换成json类型
json_str = json.loads(str_json)

print(json_str)

# 测试取json值。
print(json_str["od"]["od1"])