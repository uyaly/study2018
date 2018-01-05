# coding:utf-8
# !/usr/bin/env Python
from appium import webdriver
import time
# from appium.webdriver.common.touch_action import TouchAction
import sys
reload(sys)
sys.setdefaultencoding('utf8')

title = [
        u"Day166K. Home for a bee解释.m4a",
        u"Day166. I like to jump解释.m4a",
        u"Day166K. Home for a bee.m4a",
        u"Day166. I like to jump.m4a"
         ]
# 反序排列
title = [i for i in reversed(title)]

print title