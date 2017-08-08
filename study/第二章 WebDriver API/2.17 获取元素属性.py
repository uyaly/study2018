# coding:utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
time.sleep(2)
title = driver.title
print title
text = driver.find_element_by_id("setf").text
print text
# 获取元素的标签
tag = driver.find_element_by_id("kw").tag_name
print tag
# 获取元素的其它属性
name = driver.find_element_by_id("kw").get_attribute("class")
print name
# 获取输入框的内容
driver.find_element_by_id("kw").send_keys("yoyoketang")