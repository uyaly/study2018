# coding:utf-8
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("https://kyfw.12306.cn/otn/index/init")
# 去掉元素的readonly属性
js = 'document.getElementById("train_date").removeAttribute("readonly");'
driver.execute_script(js)
print js.
# 用js方法输入日期
js_value = 'document.getElementById("train_date").value="2016-12-25"'
driver.execute_script(js_value)
# # 清空文本后输入值
# driver.find_element_by_id("train_date").clear()
# driver.find_element_by_id("train_date").send_keys("2016-12-25")