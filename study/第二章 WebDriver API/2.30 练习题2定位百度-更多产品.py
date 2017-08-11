# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
e = driver.find_element_by_link_text("更多产品")
# 鼠标悬停,perform() 执行所有ActionChains中的行为
ActionChains(driver).move_to_element(e).perform()
time.sleep(1)
# ele = driver.find_element_by_name("tj_more")
# 经确认，是可以定位到元素的
# print ele.text
# 这一步点击失效了
# ele.click()
# js大法好，完美解决click失效问题
# 这个name属性未找到，好奇妙的定位
js = "document.getElementsByName('tj_more')[0].click()"
# js = "document.getElementByClassName('s_bdbrievenmore').click()"
driver.execute_script(js)