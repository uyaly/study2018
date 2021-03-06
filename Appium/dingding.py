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
                # 'deviceName': '11642f40', # 自己的小米4
                # 'deviceName': 'cc2ae2f4', # 测试机小米4
                'deviceName': '11642f40', # 测试机小米4
                # android系统的版本号
                'platformVersion': '6.0.1',
                # apk包名
                'appPackage': 'com.alibaba.android.rimet',
                # apk的launcherActivity
                'appActivity': 'com.alibaba.android.rimet.biz.SplashActivity'
                }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# time.sleep(5)
try:
    # 进入登录
    driver.find_element_by_name(u"登录").click()
except:
    pass
try:
    # print(driver.current_activity)
    driver.wait_activity("com.alibaba.android.user.login.SignUpWithPwdActivity", 10)  # 等待未登录页面
    # 输入账号密码
    driver.find_element_by_id("com.alibaba.android.rimet:id/et_phone_input").send_keys("18062427385")
    driver.find_element_by_id("com.alibaba.android.rimet:id/et_pwd_login").send_keys("123456")
    # 点击登录按钮
    driver.find_element_by_id("com.alibaba.android.rimet:id/btn_next").click()
except:
    print("Default login")
    pass


# driver.current_activity
driver.wait_activity(".biz.home.activity.HomeActivity", 20)  # 等待登录后页面
driver.find_elements_by_id("com.alibaba.android.rimet:id/home_bottom_tab_icon_group")[2].click()  # 点击“长江智联”
time.sleep(3)
try:
    driver.find_element_by_android_uiautomator('new UiSelector().description("考勤打卡")').click()
except:
    # print("考勤打卡元素找不到，坐标点击")
    driver.tap([(415, 1067)], 10)  # 点击“考勤打卡”
    pass

time.sleep(5)
driver.wait_activity("com.alibaba.lightapp.runtime.activity.CommonWebViewActivity", 10)  # 等待考勤打卡页面
if (t.hour < 9 and t.hour > 7):  # 上班时间
    try:
        driver.find_element_by_android_uiautomator('new UiSelector().description("上班打卡")').click()  # 点击上班打卡
        print("*** " + time.strftime("%H:%M:%S", time.localtime()) + " SUCCESS go to work, Manual punch the clock ***")
    except:
        # print("上班打卡元素找不到，坐标点击")
        driver.tap([(600, 680)], 10)  # 点击“上班打卡”
        print("*** SUCCESS go to work, quickly punch the clock ***")
        pass

elif (t.hour < 18 and t.hour >= 17): # 下班时间
    time.sleep(2)
    try:
        driver.find_element_by_android_uiautomator('new UiSelector().description("下班打卡")').click()# 点击”下班打卡“
        print("*** " + time.strftime("%H:%M:%S", time.localtime()) + " SUCCESS go off work, Manual punch the clock ***")
    except:
        print("下班打卡元素找不到，坐标点击")
        driver.tap([(538, 1236)], 10)  # 点击“下班打卡”
        print("*** " + time.strftime("%H:%M:%S", time.localtime()) + " SUCCESS go off work, Manual punch the clock ***")
elif (t.hour < 22 and t.hour >= 18): # 下班时间
    try:
        # 点击更新
        driver.find_element_by_android_uiautomator('new UiSelector().description("更新打卡")').click()
        print("*** " + time.strftime("%H:%M:%S", time.localtime()) + " SUCCESS go off work, Update punch the clock ***")
    except:
        print("更新打卡元素找不到，坐标点击")
        driver.tap([(200, 1150)], 10)  # 点击“更新打卡”
        print("*** " + time.strftime("%H:%M:%S", time.localtime()) + " SUCCESS go off work, Update punch the clock ***")
        pass

    time.sleep(2)

    try:
        driver.find_element_by_id("android:id/button1").click()  #  确定更新打卡
    except:
        pass

else:
    print("*** No operation ***")
    pass

time.sleep(3)
# 登出
driver.find_element_by_accessibility_id(u"返回").click()
try:
    driver.find_element_by_accessibility_id(u"返回").click()
except:
    # print("***返回成功，准备退出***")
    pass

driver.wait_activity(".biz.home.activity.HomeActivity", 10)  # 等待返回登录后页面
driver.find_element_by_name(u"我的").click()
time.sleep(2)
driver.swipe(0, 1600, 0, 100, 500)
time.sleep(2)
driver.find_element_by_id("com.alibaba.android.rimet:id/rl_setting").click()  # 点击 设置
time.sleep(2)
driver.swipe(0, 1600, 0, 1000, 500)
time.sleep(2)
driver.find_element_by_name(u"退出登录").click()
time.sleep(2)
driver.find_element_by_name(u"确认").click()
# 结束
driver.quit()