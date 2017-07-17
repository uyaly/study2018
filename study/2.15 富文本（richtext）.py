# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
profileDir = r'C:\Users\think_uyaly\AppData\Roaming\Mozilla\Firefox\Profiles\p7wm71lv.default'
profile = webdriver.FirefoxProfile(profileDir)
driver = webdriver.Firefox(profile)
bolgurl = "http://www.cnblogs.com/"
uyalybolg = bolgurl + "uyaly"
driver.get(uyalybolg)
driver.find_element_by_id("blog_nav_newpost").click()
time.sleep(5)
edittile = u'Selenium2+python自动化'
editbody = u"这里是正文内容"
driver.find_element_by_id("Editor_Edit_txbTitle").send_keys(edittile)
driver.switch_to.frame("Editor_Edit_EditorBody_ifr")
driver.find_element_by_id("tinymce").send_keys(editbody)
