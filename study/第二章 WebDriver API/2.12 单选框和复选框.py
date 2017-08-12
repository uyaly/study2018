# coding:utf-8
from selenium import webdriver
url = "file:///d:/PycharmProjects/study/eg/2_12.html"
driver = webdriver.Firefox()
driver.get(url)
driver.implicitly_wait(10)
# 没点击操作前，判断选项框状态
s = driver.find_element_by_id("boy").is_selected()
# print(s)
driver.find_element_by_id("boy").click()
# 没点击操作前，判断选项框状态
r = driver.find_element_by_id("boy").is_selected()
# print(r)
# 复选框 单选
driver.find_element_by_id("c1").click()
# 复选框，全选，find_elements
checkboxs = driver.find_elements_by_xpath(".//*[@type='checkbox']")
for i in checkboxs:
    # 全选，不执行这句是反选
    if not i.is_selected():
        i.click()