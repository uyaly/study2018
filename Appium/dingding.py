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

try:
    # 允许
    driver.wait_activity("允许", 2)
    driver.find_element_by_name("允许").click()
except:
    pass

try:
    # 进入登录
    # driver.find_element_by_id("com.alibaba.android.rimet:id/login_slide_btn").click()
    # 输入账号密码
    driver.find_element_by_id("com.alibaba.android.rimet:id/et_phone_input").send_keys("18062427385")
    driver.find_element_by_id("com.alibaba.android.rimet:id/et_pwd_login").send_keys("123456")
    # 点击登录按钮
    driver.find_element_by_id("com.alibaba.android.rimet:id/btn_next").click()

except:
    print("Default login")
    pass

try:
    driver.find_element_by_name("查看详情").click()
    # 同意
    driver.wait_activity("同意", 2)
    driver.find_element_by_android_uiautomator('new UiSelector().description("同意")').click()
except:
    pass

try:
    driver.wait_activity("允许", 2)
    # 允许
    driver.find_element_by_name("允许").click()
    driver.wait_activity("允许", 2)
    # 允许
    driver.find_element_by_name("允许").click()
except:
    pass

driver.wait_activity("com.alibaba.android.rimet:id/home_bottom_tab_button_work", 10)
driver.find_element_by_id("com.alibaba.android.rimet:id/home_bottom_tab_button_work").click()
driver.wait_activity("考勤打卡", 2)
driver.find_element_by_android_uiautomator('new UiSelector().description("考勤打卡")').click()
try:
    driver.wait_activity("我知道了", 10)
    driver.find_element_by_name("我知道了").click()
except:
    pass

if (t.hour < 10 and t.hour > 7):
    try:
        driver.wait_activity("上班打卡", 5)
        driver.find_element_by_android_uiautomator('new UiSelector().description("上班打卡")').click()
        driver.tap([(440, 1500)], 10)  # 确认打卡成功
        print("*** Go to work, Manual punch the clock, success at" + str(t) + "***")
    except:
        print("*** Go to work, quickly punch the clock, success at" + str(t) + "***")
        pass
elif (t.hour < 22 and t.hour >= 17):
    try:
        driver.wait_activity("下班打卡", 5)
        driver.find_element_by_android_uiautomator('new UiSelector().description("下班打卡")').click()
        driver.tap([(440, 1500)], 10)  # 确认打卡成功
        print("*** Go off work, Manual punch the clock, success at" + str(t) + "***")
    except:
        driver.wait_activity("更新打卡", 5)
        driver.find_element_by_android_uiautomator('new UiSelector().description("更新打卡")').click()
        driver.find_element_by_name(u"确定").click()
        driver.tap([(440, 1500)], 10)  # 确认打卡成功
        print("*** Go off work, Update punch the clock, success at" + str(t) + "***")
        # print("*** No operation ***")
        pass
else:
    print("*** No operation ***")
    pass

# 登出
driver.wait_activity("返回", 5)
driver.find_element_by_name(u"返回").click()
driver.find_element_by_name(u"我的").click()
driver.swipe(0, 1622, 0, 530, 500)
driver.find_element_by_id("com.alibaba.android.rimet:id/rl_setting").click() # 设置
driver.find_element_by_name(u"退出登录").click()
driver.find_element_by_name(u"确认").click()
driver.quit()