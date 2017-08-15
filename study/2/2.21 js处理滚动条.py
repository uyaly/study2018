# coding:UTF-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://www.baidu.com/s?wd=fiddler%E6%8A%93%E5%8C%85%E5%B7%A5%E5%85%B7&rsv_spt=1&rsv_iqid=0xeac8b28a0000b7e8&issp=1&f=3&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=98010089_dg&ch=12&rsv_enter=1&rsv_sug3=1&rsv_sug1=1&rsv_sug7=001&rsv_sug2=1&rsp=4&rsv_sug9=es_2_1&inputT=2071&rsv_sug4=4652&rsv_sug=9")
print driver.name

# 回到顶部
def scroll_top():
    if driver.name == "chrome":
        js = "var q = document.bady.scrolltop = 0"
    else:
        js = "var q = document.documentElement.scrollTop = 0"
    return driver.execute_script(js)
# 拉到底部
def scroll_top():
    if driver.name == "chrome":
        js = "var q = document.bady.scrolltop = 10000"
    else:
        js = "var q = document.documentElement.scrollTop = 10000"
    return driver.execute_script(js)
# 滚动到底部
js = "window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(js)
# 滚动到顶部
js = "window.scrollTo(0,0)"
driver.execute_script(js)
# 聚焦元素
target = driver.find_element_by_id('u')
driver.execute_script("arguments[0].scrollIntoView();", target)
print(target)