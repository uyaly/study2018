# coding:utf-8
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://mail.126.com/")
driver.implicitly_wait(20)
driver.switch_to.frame("x-URS-iframe")
# 方法一：取单个class属性
driver.find_element_by_class_name("dlemail").send_keys("yoyo")
driver.find_element_by_class_name("dlpwd").send_keys("12333")
# 方法二：定位一组取下标定位（乃下策）
# driver.find_elements_by_class_name("j-inputtext")[0].send_keys("yoyo")
# driver.find_elements_by_class_name("j-inputtext")[1].send_keys("12333")
# 方法三：css定位
# driver.find_element_by_css_selector(".j-inputtext.dlemail").send_keys("yoyo")
# driver.find_element_by_css_selector(".j-inputtext.dlpwd").send_keys("123")
# 方法四：取单个class属性也是可以的
# driver.find_element_by_css_selector(".dlemail").send_keys("yoyo")
# driver.find_element_by_css_selector(".dlpwd").send_keys("123")