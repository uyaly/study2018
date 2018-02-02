# coding:utf-8
import requests
# 加两行，屏蔽告警
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# 先打开登录首页，获取部分cookie
url = "https://passport.cnblogs.com/user/signin"
headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0" }

url = "https://passport.cnblogs.com/user/signin"
headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0)Gecko/20100101 Firefox/44.0"} # get方法其它加个ser-Agent就可以了
s = requests.session()
r = s.get(url, headers=headers,verify=False)
# print s.cookies

# 添加登录需要的两个cookie
c = requests.cookies.RequestsCookieJar()
c.set('.CNBlogsCookie', '03F5C3956AFDB5371B8D4911F87BF3D731C505CF169875296FD6D909B23D42884DBB9A151EFFE16C7F41374D9A20BF49F662DD4919CEB907F4C1E2239B990E89AC85BAB6F9D952F186A72C6E307A7144F18F5E09') # 填上面抓包内容
c.set('.Cnblogs.AspNetCore.Cookies',
      'CfDJ8N7AeFYNSk1Put6Iydpme2ZoY8lL7UPsLjF1FLQZCew9kZU93OlJcpEBA4Lr8sqjkbaxbJ20H9dUsMqi5HJPlPUDVv3H9JmCZhvf7lFSwL8JcYdvu1-B-DjcD8ohrAIIrdORdbT9Mio3usks0yZ9igqHnwJ9mNPAk3HHO9x6lPwLhNODtgQ8IpxXbrOuoVR1RBFyXCwBmaHBHaIKD4pY_QvW0NopUWKnmLHm9Q6K0JZXYyBS9W-nw5o5fwyQHZdM5MInq-AFZgDjZ2_WDhZbV_sxYF2MViofunoz2GAysLRvO7w0j4AnM7k5Rd8Mjd9DaQ')
# 填上面抓包内容
c.set('AlwaysCreateItemsAsActive', "True")
c.set('AdminCookieAlwaysExpandAdvanced', "True")
s.cookies.update(c)
# print s.cookies

# 登录成功后保存编辑内容
r1 = s.get("https://i.cnblogs.com/EditPosts.aspx?opt=1", headers=headers, verify=False)

# 保存草稿箱
url2 = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
body = {"__VIEWSTATE": "",
        "__VIEWSTATEGENERATOR":"FE27D343",
        "Editor$Edit$txbTitle":"这是3111",
        "Editor$Edit$EditorBody":"<p>这里111：http://www.cnblogs.com/yoyoketang/</p>",
        "Editor$Edit$Advanced$ckbPublished":"on",
        "Editor$Edit$Advanced$chkDisplayHomePage":"on",
        "Editor$Edit$Advanced$chkComments":"on",
        "Editor$Edit$Advanced$chkMainSyndication":"on",
        "Editor$Edit$Advanced$txbEntryName":"",
        "Editor$Edit$Advanced$txbExcerpt":"",
        "Editor$Edit$Advanced$tbEnryPassword":"",
        "Editor$Edit$lkbDraft":"存为草稿", }
r2 = s.post(url2, data=body, verify=False)
print r.content