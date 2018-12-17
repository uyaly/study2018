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
                'deviceName': 'cc2ae2f4', # 测试机小米4
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
    # driver.find_element_by_id("com.alibaba.android.rimet:id/login_slide_btn").click()
    # 输入账号密码
    driver.wait_activity("com.alibaba.android.rimet:id/et_phone_input", 10)
    driver.find_element_by_id("com.alibaba.android.rimet:id/et_phone_input").send_keys("18062427385")
    driver.find_element_by_id("com.alibaba.android.rimet:id/et_pwd_login").send_keys("123456")
    # 点击登录按钮
    driver.find_element_by_id("com.alibaba.android.rimet:id/btn_next").click()
    # driver.find_element_by_android_uiautomator('new UiSelector().description("同意")').click()
    # driver.find_elements_by_class_name("android.view.View")[231].click()
    # time.sleep(3)
    # driver.tap([(1000, 1800)], 10)  # 点击右下角“同意”
except:
    print("Default login")
    pass

# driver.tap([(520, 1800)], 10)
time.sleep(5)
driver.wait_activity("com.alibaba.android.rimet:id/home_bottom_tab_icon_group", 10)
driver.find_elements_by_id("com.alibaba.android.rimet:id/home_bottom_tab_icon_group")[2].click()  # 点击“长江智联”
# print("长江智联进去的页面list：")
# print(driver.contexts)
driver.tap([(415, 1067)], 10)  # 点击“考勤打卡”
# print("考勤打卡进去的页面list：")
# print(driver.contexts)
# 允许
# time.sleep(5)
# driver.wait_activity("ndroid.widget.Button", 5)
# driver.find_elements_by_class_name("android.widget.Button")[1].click()   # 点击 允许

time.sleep(10)
if (t.hour < 10 and t.hour > 7):
    try:
        driver.tap([(600, 680)], 10)  # 点击“上班打卡”
        print("*** Go to work, Manual punch the clock, success at" + str(t) + "***")
    except:
        # 找不到
        print("*** Go to work, quickly punch the clock, success at" + str(t) + "***")
        pass

elif (t.hour < 22 and t.hour >= 17):
    try:
        driver.tap([(550, 150)], 10)  # 点击“下班打卡”
        print("*** Go off work, Manual punch the clock, success at" + str(t) + "***")
    except:
        driver.tap([(415, 1491)], 10)  # 点击“更新打卡”
        driver.wait_activity(u"确定", 5)
        driver.find_element_by_name(u"确定").click()
        print("*** Go off work, Update punch the clock, success at" + str(t) + "***")

        pass
else:
    print("*** No operation ***")
    pass

# try:
#     driver.tap([(440, 1500)], 10)  # 确认打卡成功
#     print("***打卡成功***")
# except:
#     pass

# 登出
driver.wait_activity("返回", 5)
driver.find_element_by_name(u"返回").click()

try:
    driver.find_element_by_name(u"返回").click()
except:
    print("***返回成功，准备退出***")
    pass

driver.wait_activity("我的", 5)
driver.find_element_by_name(u"我的").click()
driver.swipe(0, 1622, 0, 530, 500)
driver.find_element_by_id("com.alibaba.android.rimet:id/rl_setting").click()  # 设置
driver.find_element_by_name(u"退出登录").click()
driver.find_element_by_name(u"确认").click()
# 结束
driver.quit()