# coding:utf-8
from appium import webdriver
import datetime
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
t = datetime.datetime.now()
desired_caps = {
                # 这里是声明android还是ios的环境
                'platformName': 'Android',
                # 手机设备名称，通过adb devices查看
                'deviceName': '11642f40',
                # android系统的版本号
                'platformVersion': '6.0.1',
                # apk包名
                'appPackage': 'com.alibaba.android.rimet',
                # apk的launcherActivity
                'appActivity': 'com.alibaba.android.rimet.biz.SplashActivity'
                }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(5)

try:
    # 输入密码
    driver.find_element_by_id("com.alibaba.android.rimet:id/et_pwd_login").send_keys("123456")
    # 点击登录按钮
    driver.find_element_by_id("com.alibaba.android.rimet:id/btn_next").click()
except:
    print("Default login")
    pass
time.sleep(5)
# print ("打卡时间"+ str(t))

driver.find_element_by_id("com.alibaba.android.rimet:id/home_bottom_tab_button_work").click()
time.sleep(2)
driver.find_element_by_android_uiautomator('new UiSelector().description("考勤打卡")').click()
time.sleep(10)
if (t.hour < 8 or t.hour == 8):
    try:
        driver.find_element_by_android_uiautomator('new UiSelector().description("上班打卡")').click()
        print("*** Go to work, Manual punch the clock, success at" + str(t) + "***")
    except:
        print("*** Go to work, quickly punch the clock, success at" + str(t) + "***")
        pass
else:
    try:
        driver.find_element_by_android_uiautomator('new UiSelector().description("下班打卡")').click()
        print("*** Go off work, Manual punch the clock, success at" + str(t) + "***")
    except:
        driver.find_element_by_android_uiautomator('new UiSelector().description("更新打卡")').click()
        driver.find_element_by_name(u"确定").click()
        print("*** Go off work, Update punch the clock, success at" + str(t) + "***")
        # print("*** No operation ***")
        pass
time.sleep(5)
driver.quit()