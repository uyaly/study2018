# coding:utf-8
from selenium import webdriver

driver = webdriver.Firefox()
base_url = "http://mail.163.com"
# 打开浏览器
driver.get(base_url)
driver.implicitly_wait(10)
# tag切换iframe
iframe = driver.find_element_by_tag_name("iframe")
driver.switch_to.frame(iframe)
# id切换iframe
# driver.switch_to.frame("x-URS-iframe")
driver.find_element_by_name("email").send_keys("123")
driver.find_element_by_name("password").send_keys("456")
# 释放iframe，重新回到主页上
driver.switch_to.default_content()
# 关闭浏览器
driver.quit()