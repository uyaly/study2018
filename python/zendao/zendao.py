# -*- coding: utf-8 -*-

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

    def get_bugs(slef):
        """
        获取所有BUG
        :return:
        """
        url = slef.host + "bug-browse-13-0-all-0--2000-2000-1.json"
        loginResp = json.loads(slef.s.get(url).content)
        data = loginResp['data']
        data_json = json.loads(data)['bugs']
        return data_json

    def bugs_lists(slef):
        """
        对获取的BUG处理，过滤出需要的字段，重新返回列表bugs_list
        :return:
        """
        bugs_list = []
        for bug in slef.get_bugs():
            title = bug['title']
            severity = bug['severity']
            status = bug['status']
            bug_dict = {'title': title, 'severity': severity, 'status': status}
            bugs_list.append(bug_dict)
        return bugs_list

    def count_bugs(self, *args):
        """
        需要的数据：功能项，BUG各状态条数，BUG状态对应的关闭数
        输入：功能项标题
        统计：BUG各状态计数，BUG状态下关闭数计数
        输出：所有功能项对应统计数，列表显示，如：
        [['【用户管理】', 0, 0, 6, 5, 8, 5, 0, 0], ['【单位管理】', 0, 0, 7, 7, 10, 8, 1, 1]]
        :param args: BUG标题包含列表
        :return:
        """
        count_list = []
        for title in args:
            s_1_status_closed_count = 0
            s_2_status_closed_count = 0
            s_3_status_closed_count = 0
            s_4_status_closed_count = 0

            severity_1_count = 0
            severity_2_count = 0
            severity_3_count = 0
            severity_4_count = 0
            for bug in self.bugs_lists():
                if title in bug['title']:
                    if bug['severity'] == '1':
                        severity_1_count += 1
                        if bug['status'] == 'closed':
                            s_1_status_closed_count += 1
                    elif bug['severity'] == '2':
                        severity_2_count += 1
                        if bug['status'] == 'closed':
                            s_2_status_closed_count += 1
                    elif bug['severity'] == '3':
                        severity_3_count += 1
                        if bug['status'] == 'closed':
                            s_3_status_closed_count += 1
                    elif bug['severity'] == '4':
                        severity_4_count += 1
                        if bug['status'] == 'closed':
                            s_4_status_closed_count += 1
            title_count_list = [title, severity_1_count, s_1_status_closed_count,
                                severity_2_count, s_2_status_closed_count,
                                severity_3_count, s_3_status_closed_count,
                                severity_4_count, s_4_status_closed_count,
                                ]
            count_list.append(title_count_list)

        return count_list


if __name__ == '__main__':
    s = requests.session()
    z = ZenTao(s, "http://192.168.3.212/zentaopms/www/", "liuy", "liuyan")
    z.get_zentaosid()
    print(z.count_bugs(*["【用户管理】", "【单位管理】"]))