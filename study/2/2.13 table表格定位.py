# coding:utf-8
from selenium import webdriver
import time
url = "file:///d:/PycharmProjects/study/eg/2_13.html"
driver = webdriver.Firefox()
driver.get(url)
time.sleep(3)
t = driver.find_element_by_xpath(".//*[@id='myTable']/tbody/tr[1]/th[1]")
print(t.text)


