# coding:utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox()
driver.get("http://www.cnblogs.com/yoyoketang")
# 判断title完全等于
title = EC.title_is(u'上海-悠悠 - 博客园')
print title(driver)
# 判断title包含
title1 = EC.title_contains(u'上海-悠悠')
print title1(driver)
# 另外一种写法
r1 = EC.title_is(u'上海-悠悠 - 博客园')(driver)
r2 = EC.title_contains(u'上海-悠悠')(driver)
print r1
print r2
