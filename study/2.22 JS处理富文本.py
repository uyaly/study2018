# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# 配置文件地址
profile_directory = r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\331b4lm9.default'
# 加载配置配置
profile = webdriver.FirefoxProfile(profile_directory)
# 启动浏览器配置
driver = webdriver.Firefox(profile)
blogurl = "http://www.cnblogs.com/"
uyalyblog = blogurl + "uyaly"
driver.get(uyalyblog)
driver.find_element_by_id("blog_nav_newpost").click()
time.sleep(5)

edittile = u"Selenium2+python自动化23-富文本"
editbody = u"这里是发帖的正文"
driver.find_element_by_id("Editor_Edit_txbTitle").send_keys(edittile)
body = "这里是通过js发的正文内容"
# js处理iframe问题（js代码太长了，我分成两行了）
js = 'document.getElementById("Editor_Edit_EditorBody_ifr")' \
    '.contentWindow.document.body.innerHTML="%s"' % body
driver.execute_script(js)
# 保存草稿
driver.find_element_by_id("Editor_Edit_lkbDraft").click()