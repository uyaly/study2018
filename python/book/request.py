# encoding:UTF-8
import requests
# 新建一个session对象（就像开了一个浏览器一样）
session = requests.Session()
# 使用get方法获取https://www.baidu.com/s?wd=python
url = 'http://39.108.224.133/'
params = { 'token': 'wechat', }
r = session.get(url = url, params = params)
with open('home.htm') as f: f.write(r.content) # 存入文件，可以使用浏览器尝试打开
# 举例使用post方法
import json
url = 'https://www.baidu.com'
data = { 'wd': 'python', }
r = session.get(url = url, data = json.dumps(data))
with open('home.htm') as f: f.write(r.content)
# 以上代码与下面的代码不连续