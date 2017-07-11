# coding:utf-8
from selenium import webdriver
import time
url = "file:///F:/PycharmProjects/test/eg/1.html"
driver = webdriver.Firefox()
driver.get(url)
time.sleep(3)
driver.find_element_by_id("prompt").click()
time.sleep(4)
# t = driver.switch_to_alert()
t = driver.switch_to.alert
# 打印警告框文本内容
print(t.text)
t.send_keys("hello selenium2")
# 点击警告框确认按钮
t.accept()
# t.dismiss()相当于点x按钮，取消