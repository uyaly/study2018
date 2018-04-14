# coding:utf-8
# !/usr/bin/env Python
from appium import webdriver
import time
# from appium.webdriver.common.touch_action import TouchAction
import sys
reload(sys)
sys.setdefaultencoding('utf8')
titles = []
title = [
        "Day166K. Home for a bee解释.",
        u"Day166. I like to jump解释",
        u"Day166K. Home for a bee.",
        u"Day166. I like to jump."
         ]
for j in range(len(title)):
    titles.append(title[j] + ".m4a")
    j = j+1
# 反序排列

title = [i + ".m4a" for i in reversed(title)]
for i in title:
    print i