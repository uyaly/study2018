# coding:utf-8
from selenium import webdriver
import time
# 配置文件地址
profile_directory = r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\331b4lm9.default'
# 加载配置配置
profile = webdriver.FirefoxProfile(profile_directory)
# 启动浏览器配置
driver = webdriver.Firefox(profile)

bolgurl = "http://www.cnblogs.com"
yoyobolg = bolgurl + "yoyoketang"
driver.get(yoyobolg)
driver.find_element_by_id("blog_nav_newpost").click()
time.sleep(5)
edittile = u'Selenium2+python自动化23-富文本'
editbody = u"这里是发帖的正文"
driver.find_element_by_id("Editor_Edit_txbTitle").send_keys(edittile)
driver.switch_to.frame("Editor_Edit_EditorBody_ifr")
# 有些小伙伴可能输入不成功，可以在输入之前先按个table键，send_keys(Keys.TAB)
# driver.find_element_by_id("tinymce").send_keys(Keys.TAB)
driver.find_element_by_id("tinymce").send_keys(editbody)