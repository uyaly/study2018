# coding:utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://www.cnblogs.com/uyaly")
# # 添加cookie
c1 = {u'domain': u'.cnblogs.com',
    u'name': u'.CNBlogsCookie',
    u'value': u'B6531C49D1197836795F3BCA756CDEA55C002E31C674BCCC6400A9E3E2556E37F5A79E771637F36144F92367B057C5E91DCC3A11E2F3EC96EDAAB5860D0CA2EDC0C46D848A19867C8D816862890424AA7E26832A',
    u'expiry': 1502088720,u'path': u'/',u'httpOnly': True,u'secure': False}
c2 = {u'domain': u'.cnblogs.com',
    u'name': u'.Cnblogs.AspNetCore.Cookies',
    u'value': u'CfDJ8PhlBN8IFxtHhqIV3s0LCDl0idGgf_-u75Ic0_yLiIpoyFppF_GIcgO4us997WR3qVRMdJ5ngU68uqWwW6M3AvRE_zA1YZ1PSUpE58iM2aSqkGk4eQUnvga2AjH8T5VaLXF0TXK_TIr2bx3gaQ3-FywI7Sk6xH4rpJirLF9DOm8Ii2psub5MOSglqmi9-SzmSuJRf8JTvVqv_rpF9CzG5Y8GhY5SHzNqVHanPBoPyj0amiblIRuAneYaPWImBzFJf_akIOgpGuGGP-JCCJjDJvantoythGKqaIQes_gq5tju',
    u'expiry': 1502088720,u'path': u'/',u'httpOnly': True,u'secure': False}
# 添加2个值
driver.add_cookie(c1)
driver.add_cookie(c2)
time.sleep(3)
# 刷新下页面就见证奇迹了
driver.refresh()
# 1.登录时候要勾选下次自动登录按钮。
# 2.add_cookie（）只添加name和value，对于博客园的登录是不成功。
# 3.本方法并不适合所有的网站，一般像博客园这种记住登录状态的才会适合。