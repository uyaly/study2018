# coding:utf-8
from appium import webdriver
import time
desired_caps = {
                # 这里是声明android还是ios的环境
                'platformName': 'Android',
                # 手机设备名称，通过adb devices查看
                'deviceName': '11642f40',
                # android系统的版本号
                'platformVersion': '6.0.1',
                # apk包名
                'appPackage': 'com.yibasan.lizhifm',
                # apk的launcherActivity
                'appActivity': 'com.yibasan.lizhifm.activities.EntryPointActivity'
                }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# 休眠15秒等待页面加载完成
time.sleep(5)
# button = driver.find_elements_by_class_name("android.widget.LinearLayout")
driver.find_element_by_id("com.yibasan.lizhifm:id/header_user_icon").click()
driver.find_element_by_id("com.yibasan.lizhifm:id/followLabel").click()
driver.find_element_by_id("com.yibasan.lizhifm:id/user_fans_user_head").click()

# android.widget.TextView
driver.find_element_by_link_text(u"声音").click()
driver.quit()