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
                'appPackage': 'com.android.fileexplorer',
                # apk的launcherActivity
                'appActivity': 'com.android.fileexplorer.FileExplorerTabActivity'
                }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# 休眠15秒等待页面加载完成
time.sleep(5)
driver.find_element_by_name("手机").click()
driver.find_element_by_name("183").click()
driver.find_element_by_name("LizhiFM").click()
driver.find_element_by_name("Files").click()
driver.find_element_by_name("download").click()
# 长按文件重命名


time.sleep(5)
driver.quit()