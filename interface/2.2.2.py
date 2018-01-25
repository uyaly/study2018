# coding:utf-8
import requests

# payload参数是字典类型，传到form里
payload = {"yoyo": "hello world",
           "pythonQQ群": "226666666"}

r = requests.post("http://httpbin.org/post", data=payload)
print r.text