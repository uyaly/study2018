# coding:utf-8
from appium import webdriver
import time
desired_caps = {
                'platformName': 'Android',
                'deviceName': '11642f40',
                'platformVersion': '6.0.1',
                # apk包名
                # 'appPackage': 'com.yibasan.lizhifm',
                # apk的launcherActivity
                # 'appActivity': 'com.yibasan.lizhifm.activities.EntryPointActivity'
                }
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# 获取屏幕的size
# size = driver.get_window_size()
# print(size)
# # 屏幕宽度width
# print(size['width'])
# # 屏幕高度width
# print(size['height'])
def swipeUpLiZhi(driver, t=500, n=1):
    '''向上滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.5      # x坐标
    y1 = 1622    # 起始y坐标
    # y2 = 369   # 终点y坐标
    y2 = 530   # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)
def swipeUp(driver, t=500, n=1):
    '''向上滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.5      # x坐标
    y1 = l['height'] * 0.75    # 起始y坐标
    y2 = l['height'] * 0.25    # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)
def swipeDown(driver, t=500, n=1):
    '''向下滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.5         # x坐标
    y1 = l['height'] * 0.25       # 起始y坐标
    y2 = l['height'] * 0.75       # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2,t)
def swipLeft(driver, t=500, n=1):
    '''向左滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.75
    y1 = l['height'] * 0.5
    x2 = l['width'] * 0.05
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)
def swipRight(driver, t=500, n=1):
    '''向右滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.05
    y1 = l['height'] * 0.5
    x2 = l['width'] * 0.75
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)

if __name__ == "__main__":
    print(driver.get_window_size())
    time.sleep(10)
    swipeUp(driver, n=2)