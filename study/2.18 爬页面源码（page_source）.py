# coding:utf-8
from selenium import webdriver
# re非贪婪模式，正则匹配
import re
driver = webdriver.Firefox()
driver.get("http://www.cnblogs.com/uyaly/")
# selenium的page_source方法可以直接返回页面源码
page = driver.page_source
# print page
# "非贪婪匹配,re.S('.'匹配字符,包括换行符)"
url_list = re.findall('href=\"(.*?)\"', page, re.S)
url_all = []
for url in url_list:
    if "http" in url:
        print url
        url_all.append(url)
# 最终的url集合
print url_all