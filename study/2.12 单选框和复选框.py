# coding:utf-8
from selenium import webdriver
url = "file:///F:/PycharmProjects/test/eg/2_12.html"
driver = webdriver.Firefox()
driver.get(url)
driver.implicitly_wait(10)
# 单选框，先选男孩，等10秒再选女孩
driver.find_element_by_id("boy").click()
driver.implicitly_wait(10)
driver.find_element_by_id("girl").click()
# 复选框，全选
checkboxs = driver.find_element_by_xpath(".//*[@type='checkbox']")
for i in checkboxs:
    # checkboxs.is_selected() == "false"
    i.click()

