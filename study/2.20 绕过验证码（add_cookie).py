# coding:utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://www.cnblogs.com/uyaly")
# # 添加cookie
c1 = {u'domain': u'.cnblogs.com',
    u'name': u'.CNBlogsCookie',
    u'value': u'xxxx',
    u'expiry': 1491887887,
    u'path': u'/',
    u'httpOnly': True,
    u'secure': False}
c2 = {u'domain': u'.cnblogs.com',
    u'name': u'.Cnblogs.AspNetCore.Cookies',
    u'value': u'xxxx',
    u'expiry': 1491887887,
    u'path': u'/',
    u'httpOnly': True,
    u'secure': False}
# 添加2个值
driver.add_cookie(c1)
driver.add_cookie(c2)
time.sleep(3)
# 刷新下页面就见证奇迹了
driver.refresh()