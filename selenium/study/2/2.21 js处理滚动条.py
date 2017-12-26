# coding:UTF-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=1&rsv_pq=80aeb9d60002da5f&rsv_t=afdd7APRUxS4ay7ucviQYB7wUByCP6K93GzYeCr8ONLQZt%2FhImO%2FNF94b1Y&rqlang=cn&rsv_enter=0&rsv_sug3=1&rsv_sug1=1&rsv_sug7=100&inputT=1424&rsv_sug4=1424")
print driver.name

# # 回到顶部
# def scroll_top():
#     if driver.name == "chrome":
#         js = "var q = document.bady.scrolltop = 0"
#     else:
#         js = "var q = document.documentElement.scrollTop = 0"
#     return driver.execute_script(js)
# # 拉到底部
# def scroll_top():
#     if driver.name == "chrome":
#         js = "var q = document.bady.scrolltop = 10000"
#     else:
#         js = "var q = document.documentElement.scrollTop = 10000"
#     return driver.execute_script(js)
time.sleep(5)
# 滚动到底部
js = "window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(js)
time.sleep(3)
# 滚动到顶部
js = "window.scrollTo(0,0)"
driver.execute_script(js)
# 聚焦元素
target = driver.find_element_by_id('u')
driver.execute_script("arguments[0].scrollIntoView();", target)
print(target)