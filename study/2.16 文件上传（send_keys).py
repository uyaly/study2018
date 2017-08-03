# coding:utf-8
from selenium import webdriver
import time
profileDir = r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\331b4lm9.default'
profile = webdriver.FirefoxProfile(profileDir)
driver = webdriver.Firefox(profile)
driver.implicitly_wait(30)
driver.get("http://www.cnblogs.com/uyaly/")
driver.find_element_by_link_text("新随笔").click()
time.sleep(3)
# 点开编辑器图片
driver.find_element_by_css_selector("img.mceIcon").click()
time.sleep(3)
# 定位所有iframe，取第二个
iframe = driver.find_elements_by_tag_name('iframe')[1]
# 切换到iframe上
driver.switch_to.frame(iframe)
# 文件路径
driver.find_element_by_name('file').send_keys(r'E:\temp\1.png')