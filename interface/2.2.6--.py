# coding:utf-8
import requests
url = "https://passport.cnblogs.com/user/signin"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json; charset=utf-8",
            # "VerificationToken": "",
            "X-Requested-With": "XMLHttpRequest",
            # "Referer": "",
            "Content-Length": "385",
            "Cookie": "xxx...",   # 此处省略
            "Connection": "keep-alive"
           }
payload = {"input1": "xxx", "input2": "xxx", "remember": True}
r = requests.post(url, json=payload, headers=headers, verify=False)
print r.json()