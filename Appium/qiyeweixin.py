# coding:utf-8
from appium import webdriver
import datetime
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
t = datetime.datetime.now()
name = "oscaryou"
mm = "swim@1120"
desired_caps1 = {
                # 这里是声明android还是ios的环境
                'platformName': 'Android',
                # 手机设备名称，通过adb devices查看
                'deviceName': '11642f40',
                # android系统的版本号
                'platformVersion': '6.0.1',
                # apk包名
                'appPackage': 'com.tencent.wework',
                # apk的launcherActivity
                'appActivity': 'com.tencent.wework.launch.LaunchSplashActivity'
                # 'appWaitActivity': 'com.tencent.mm.app.WeChatSplashActivity'
                }

desired_caps2 = {
                # 这里是声明android还是ios的环境
                'platformName': 'Android',
                # 手机设备名称，通过adb devices查看
                'deviceName': '11642f40',
                # android系统的版本号
                'platformVersion': '6.0.1',
                # apk包名
                'appPackage': 'com.tencent.mm',
                # apk的launcherActivity
                'appActivity': 'com.tencent.mm.ui.LauncherUI'
                # 'appWaitActivity': 'com.tencent.mm.app.WeChatSplashActivity'
                }

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps2)

# try:
#     driver.wait_activity("登录", 5)
#     driver.find_element_by_name(u"登录").click()
#     driver.find_element_by_name(u"用微信号/QQ号/邮箱登录").click()
#     driver.find_elements_by_class_name("android.widget.EditText")[0].send_keys(name)
#     driver.find_elements_by_class_name("android.widget.EditText")[1].send_keys(mm)
#     driver.find_element_by_name(u"登录").click()
# except:
#     pass
# driver.quit()


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps1)
try:
    driver.find_element_by_name(u"微信登录").click()
    driver.find_elements_by_class_name("android.widget.EditText")[0].send_keys(name)
    driver.find_elements_by_class_name("android.widget.EditText")[1].send_keys(mm)
    driver.find_element_by_name(u"登录").click()

except:
    # print driver.find_element_by_id("com.tencent.mm:id/chb").text
    pass
driver.wait_activity("com.tencent.wework:id/cr9", 5)
driver.find_element_by_id("com.tencent.wework:id/cr9").click()
driver.wait_activity("工作台", 5)
driver.find_element_by_name(u"工作台").click()
driver.find_element_by_name(u"打卡").click()
# driver.find_element_by_name(u"下班打卡").click()
time.sleep(5)
# 结束
driver.quit()