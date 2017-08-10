# encoding:utf-8 
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://www.runoob.com/try/try.php?filename=tryjs_alert")
driver.switch_to.frame("iframeResult")
driver.find_element_by_xpath("html/body/input").click()
time.sleep(1)
# 应该是用switch_to.alert()，但是新写法却会报错:TypeError: 'Alert' object is not callable
al = driver.switch_to_alert()
time.sleep(1)
al.accept()
