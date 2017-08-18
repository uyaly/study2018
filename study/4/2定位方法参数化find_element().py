# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
driver.find_element("id", "kw").send_keys("yoyoketang")
driver.find_element('css selector', "#su").click()
# 其它定位参考
# t1 = driver.find_element("link text", "糯米").text
# print t1
# t2 = driver.find_element("name", "tj_trnews").text
# print t2
# t3 = driver.find_element("class name", "bri").text
# print t3
