# coding:utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://passport.cnblogs.com/user/signin")
driver.implicitly_wait(20)
# 输入账号
username = "$('#input1').val('上海-悠悠')"
driver.execute_script(username)
# 清空文本
# time.sleep(5)
# clear = "$('#input1').val('')"
# driver.execute_script(clear)
# 输入密码
psw = "$('#input2').val('yoyo')"
driver.execute_script(psw)
# 点击登录按钮
button = "$('#signin').click()"
driver.execute_script(button)
