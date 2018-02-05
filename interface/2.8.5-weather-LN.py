# coding:utf-8
from urllib2 import urlopen
import urllib.request
import re
import json

url = "http://www.weather.com.cn/weather/101200101.shtml"
# 获取页面返回内容
html = urllib.request.urlopen(url).read()
# 转换成utf-8
html = html.decode("utf-8")

print(html)

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