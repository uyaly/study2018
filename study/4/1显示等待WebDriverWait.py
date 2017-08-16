# coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
# 等待时长10秒，默认0.5秒询问一次
WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("kw")).send_keys("yoyo")
# 判断id为kw元素是否消失
is_disappeared = WebDriverWait(driver, 10, 1).until_not(lambda x: x.find_element_by_id("kw").is_displayed())
print is_disappeared