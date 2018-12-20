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
                'deviceName': 'cc2ae2f4',
                # android系统的版本号
                'platformVersion': '6.0.1',
                # apk包名
                'appPackage': 'com.tencent.wework',
                # apk的launcherActivity
                'appActivity': 'com.tencent.wework.launch.LaunchSplashActivity'
                # 'appWaitActivity': 'com.tencent.mm.app.WeChatSplashActivity'
                }

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps1)
try:
    time.sleep(5)
    driver.find_element_by_name(u"微信登录").click()
    driver.find_elements_by_class_name("android.widget.EditText")[0].send_keys(name)
    driver.find_elements_by_class_name("android.widget.EditText")[1].send_keys(mm)
    driver.find_element_by_name(u"登录").click()
    # driver.tap([(1000, 1800)], 10)  # 点击右下角“允许”
except:
    pass
try:
    # 进入企业
    driver.wait_activity("com.tencent.wework:id/dc6", 5)
    driver.find_element_by_id("com.tencent.wework:id/dc6").click()
    # driver.find_element_by_name(u"进入企业 ").click()
except:
    pass
driver.wait_activity("工作台", 5)
driver.find_element_by_name(u"工作台").click()
# driver.find_element_by_id("com.tencent.wework:id/ao8").click()

driver.find_element_by_name(u"打卡").click()
# driver.find_element_by_id("com.tencent.wework:id/atw").click()

driver.find_element_by_name(u"下班打卡").click()

driver.find_element_by_name(u"更新").click()
time.sleep(5)
# 结束
driver.quit()
