# driver.py
# coding:utf-8
# 自动获取设备信息apk信息，并打开apk

from appium import webdriver
import os
import re
import subprocess

def driver():
    appLocation = r"D:\ly\python\Appium\apk\taobao.apk"  # 测试包

    readDeviceId = list(os.popen('adb devices').readlines())  # 获取设备名

    deviceId = re.findall(r'^\w*\b', readDeviceId[1])[0]  # 正则表达式匹配出id信息

    curline = subprocess.Popen("cmd.exe /c" + "config.bat", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)  # 获取包名和class
    a = list(curline.stdout.readlines())
    # 获取包名
    b = str(a[2])
    c = re.findall(r'com\.*.*?\'', b)
    d = str(c)
    appPackage = (d[2:-3])
    # 获取class
    e = str(a[126])
    f = re.findall(r'com\.*.*?\'', e)
    g = str(f)
    appPackageclass = (g[2:-3])

    desired_caps = {

                    'platformName': 'Android',

                    'deviceName': readDeviceId,

                    'appPackage': appPackage,

                    'appActivity':appPackageclass,

                    'unicodeKeyboard': True,

                    'resetKeyboard': True

                    }

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver()
