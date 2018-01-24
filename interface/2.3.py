# coding:utf-8
import requests
# 先打开登录首页，获取部分cookie
url = "http://localhost:8080/jenkins/j_acegi_security_check"
headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
            }      # get方法其它加个ser-Agent就可以了
d = {"from": "",
    "j_password": "f7bcd85ebab14e2fbb6d76cc99bc5c6a",
    "j_username": "admin",
    "Jenkins-Crumb": "e677c237181756818cbbccd4296d44f1",
    "json": {"j_username": "admin",
    "j_password": "f7bcd85ebab14e2fbb6d76cc99bc5c6a",
    "remember_me": True,
    "from": "",
    "Jenkins-Crumb": "e677c237181756818cbbccd4296d44f1"},
    "remember_me": "on",
    "Submit": u"登录"
    }
s = requests.session()
r = s.post(url, headers=headers, data=d)
print r.content
