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
    time.sleep(2)
    driver.find_elements_by_class_name("android.widget.EditText")[0].send_keys(name)
    driver.find_elements_by_class_name("android.widget.EditText")[1].send_keys(mm)
    driver.find_element_by_name(u"登录").click()
    # driver.tap([(1000, 1800)], 10)  # 点击右下角“允许”
except:
    pass
try:
    # 进入企业
    time.sleep(2)
    # driver.wait_activity("com.tencent.wework:id/dc6", 5)
    # driver.find_element_by_id("com.tencent.wework:id/dc6").click()
    driver.find_element_by_name(u"进入企业 ").click()
except:
    pass
time.sleep(5)
# driver.wait_activity("工作台", 5)
driver.find_element_by_name(u"工作台").click()
# driver.find_element_by_id("com.tencent.wework:id/ao8").click()

driver.find_element_by_name(u"打卡").click()
# driver.find_element_by_id("com.tencent.wework:id/atw").click()

time.sleep(10)
if (t.hour < 9 and t.hour > 7):
    try:
        driver.find_element_by_name(u"上班打卡").click()
        print("*** Go to work, Manual punch the clock, success at" + str(t) + "***")
    except:
        print("*** Go to work, quickly punch the clock, success at" + str(t) + "***")
        pass

elif (t.hour < 23 and t.hour >= 18):
    try:
        driver.find_element_by_name(u"下班打卡").click()
        print("*** Go off work, Manual punch the clock, success at" + str(t) + "***")
    except:
        print(driver.contexts)   # 1 试试打印页面
        driver.tap([(415, 1491)], 10)  # 点击“更新打卡”
        # driver.find_element_by_android_uiautomator('new UiSelector().description("更新")').click()
        # # driver.find_element_by_name(u"更新").click()  # 点击“更新”
        # driver.find_element_by_name(u"更新下班卡").click()
        # print("*** Go off work, Update punch the clock, success at" + str(t) + "***")
        pass
else:
    print("*** No operation ***")
    pass

# 结束
driver.quit()
