# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 先登录百度，没登录时候是不会重新打开窗口的

# 加载配置文件免登陆
profileDir = r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\331b4lm9.default'
profile = webdriver.FirefoxProfile(profileDir)
driver = webdriver.Firefox(profile)

driver.get("http://www.baidu.com")

# 修改元素的target属性
# 本篇只适用于有这个target="_blank"属性链接情况
js = 'document.getElementsByClassName("mnav")[0].target="";'
driver.execute_script(js)

# 再点击链接是在原来窗口打开
driver.find_element_by_link_text("新闻").click()