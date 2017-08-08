# coding:utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("file:///F:/PycharmProjects/test/eg/2_24.html")
# 纵向底部,通过id来定位，通过控制 scrollTop的值来控制滚动条高度
js1 = 'document.getElementById("yoyoketang").scrollTop=10000'
driver.execute_script(js1)
time.sleep(5)
# 纵向顶部
js2 = 'document.getElementById("yoyoketang").scrollTop=0'
driver.execute_script(js2)
time.sleep(5)
# 横向右侧，先通过id来定位，通过控制scrollLeft的值来控制滚动条
js3 = 'document.getElementById("yoyoketang").scrollLeft=10000'
driver.execute_script(js3)
time.sleep(5)
# 横向左侧
js4 = 'document.getElementById("yoyoketang").scrollLeft=0'
driver.execute_script(js4)
time.sleep(5)
# 用class属性定位
# 获取的class返回的是list对象，取list的第一个
js5 = 'document.getElementsByClassName("scroll")[0].scrollTop=10000'
driver.execute_script(js5)
time.sleep(5)
# 控制横向滚动条位置,,,getElements
js6 = 'document.getElementsByClassName("scroll")[0].scrollLeft=10000'
driver.execute_script(js6)