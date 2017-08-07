# coding:utf-8
from selenium import webdriver
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

body = "这里是通过js发的正文内容"

# js处理iframe问题（js代码太长了，我分成两行了）
js = 'document.getElementByID("Editor_Edit_EditorBody_ifr")'\
     '.contentWindow.document.body.innerHTML="%s"' % body
driver.execute_script(js)
# 保存草稿
driver.find_element_by_id("Editor_Edit_lkbDraft").click()