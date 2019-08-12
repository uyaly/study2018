# -*- coding: utf-8 -*-
# @Author : ratel
# @time : 2019-06-03 08:59
# @file : zentao_test.py
# @software : PyCharm

import json
import requests


class ZenTao():
    """
    禅道统计类
    """
    def __init__(self, s, host, username, password):
        self.s = s
        self.host = host
        self.username = username
        self.password = password

    def get_sessions(self):
        """
         获取登录页的sessions api
         :return:
         """
        url = self.host + "api-getsessionid.json"
        getsessionid = self.s.get(url)
        # print(type(getsessionid.content))
        getsessionid_str = json.loads(getsessionid.content)
        sessionID = json.loads(getsessionid_str['data'])["sessionID"]
        return sessionID

    def get_zentaosid(self):
        """
        用户登录api
        :return:
        """
        url = self.host + "user-login.json?zentaosid=" + self.get_sessions()
        data = {"account": self.username, "password": self.password}
        req = self.s.post(url, data=data)
        get_zentaosid_str = json.loads(req.content)
        return get_zentaosid_str




if __name__ == '__main__':
    s = requests.session()
    z = ZenTao(s, "http://192.168.3.212/zentaopms/www/", "liuy", "liuyan")
    z.get_zentaosid()
    print(z.count_bugs(*["【用户管理】", "【单位管理】"]))