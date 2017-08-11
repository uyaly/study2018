# encoding:utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://sh.xsjedu.org/")
time.sleep(1)
# 将display的值设置成none就可以去除这个弹窗了
js='document.getElementById("doyoo_monitor").style.display="none";'
driver.execute_script(js)