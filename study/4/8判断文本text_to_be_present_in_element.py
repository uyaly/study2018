# coding:utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox()
url = "https://www.baidu.com"
driver.get(url)
locator = ("name", "tj_trmap")
text = u"地图"
result = EC.text_to_be_present_in_element(locator, text)(driver)
print result
# 下面是失败的案例
text1 = u"地图网"
result1 = EC.text_to_be_present_in_element(locator, text1)(driver)
print result1
locator2 = ("id", "su")
text2 = u"百度一下"
result2 = EC.text_to_be_present_in_element_value(locator2, text2)(driver)
print result2