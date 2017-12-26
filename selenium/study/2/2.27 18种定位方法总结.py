# coding:utf-8
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
# 这里是定位的单个id
element = driver.find_element_by_id("kw")
print type(element)
print element
# 这里定位是多个class
elements = driver.find_elements_by_class_name("mnav")
print type(elements)
print elements
# 这里用的css语法
s = driver.find_elements("css selector", ".mnav")
# '地图'在第四个位置
print s[3].text
s[3].click()
# 这个写法也是可以的
# driver.find_elements("css selector", ".mnav")[3].click()
