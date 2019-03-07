# -*- coding: utf-8 -*-
import json
import requests

class RobotQYK():
    def content(self, Content):  # 青云客智能聊天机器人
        url = "http://api.qingyunke.com/api.php"
        # print "Robot receive:", Content
        querystring = {"key":"free","appid":"0","msg": Content}
        payload = ""
        headers = {
            'cache-control': "no-cache",
            'Postman-Token': "7e74722c-2550-44a7-b791-ed2a216b32c4"
            }
        response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
        # print(response.encoding)
        # print(response.text)
        msg = json.loads(response.text)
        replyMsg = msg["content"].replace("{br}","\r\n")
        # print "Robot reply:",(replyMsg)
        return replyMsg
