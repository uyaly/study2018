# _*_coding:utf-8_*_
from selenium import webdriver
import datetime
import time

driver = webdriver.Firefox()


driver.get("http://192.168.3.65:12011/index.html")
driver.find_element_by_id("username").send_keys("system")
driver.find_element_by_id("password").send_keys("system@123")
driver.find_element_by_id("login_btn").click()
time.sleep(2)
driver.find_element_by_xpath(".//*[@id='mainlayout_body']/div[1]/div/div[2]/ul/li[2]").click()



