# coding:utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
# 启动浏览器后获取cookies:get_cookies()
print "启动："
print driver.get_cookies()
driver.get("http://www.cnblogs.com/uyaly/")
# 打开主页后获取cookies
print "打开主页："
print driver.get_cookies()
# 登录后获取cookies
url = "https://passport.cnblogs.com/user/signin"
driver.get(url)
driver.implicitly_wait(30)
driver.find_element_by_id("input1").send_keys("uyaly")
driver.find_element_by_id("input2").send_keys("ly612101010!")
driver.find_element_by_id("signin").click()
time.sleep(3)
print "登录后："
print driver.get_cookies()
# 获取指定name的cookies:get_cookie（name）
print "获取指定："
print driver.get_cookie(name=".CNBlogsCookie")
# 清除指定name的cookie:delete_cookie(name)
print "清除指定："
driver.delete_cookie(name=".CNBlogsCookie")
print driver.get_cookies()
# 为了验证此cookie是登录的，可以删除后刷新页面
driver.refresh()
# 清除所有cookies:delete_all_cookies()
print "清除所有："
driver.delete_all_cookies()
print driver.get_cookies()
