# coding:utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
time.sleep(1)
driver.find_element_by_id("kw").send_keys(u"博客")
# 获取百度输入框的
time.sleep(1)
bd = driver.find_elements_by_class_name("bdsug-overflow")
for i in bd:
    # 通过get_attribute()方法获取到文本信息
    print i.get_attribute("data-key")
# 点击其中的一个，如：第二个
if len(bd) > 1:
    bd[1].click()
    # 打印当前页面url
    print driver.current_url
else:
    print "未获取到匹配的词"

# class属性中间的空格并不是空字符串，那是间隔符号，表示的是一个元素有多个class的属性名称
# <div class="bdsug" style="height: auto; display: none;">
# <ul>
# <li class="bdsug-store bdsug-overflow" data-key="博客网站">
# <li class="bdsug-store bdsug-overflow" data-key="博客">
# <li class="bdsug-overflow" data-key="博客推广">
# <li class="bdsug-overflow" data-key="博客天下">
# </ul>
# </div>