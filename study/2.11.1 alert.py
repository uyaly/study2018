# coding:utf-8
from selenium import webdriver
url = "file:///F:/PycharmProjects/test/eg/1.html"
driver = webdriver.Firefox()
driver.get(url)
driver.find_element_by_id("alert").click()
# t = driver.switch_to_alert()
t = driver.switch_to.alert
# 打印警告框文本内容
print(t.text)
# 点击警告框确认按钮
t.accept()
# t.dismiss()相当于点x按钮，取消