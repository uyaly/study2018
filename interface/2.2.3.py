# coding:utf-8
import requests
import json
# post的body是json类型，也可以用json参数传入
payload = {"yoyo": "hello world",
           "pythonQQ群": "226666666"}
# 用dumps方法转化成json格式
data_json = json.dumps(payload)
r = requests.post("https://httpbin.org/post", json=data_json)
print r.text
#  返回结果，传到data里