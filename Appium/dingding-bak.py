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
    driver.wait_activity(u"登录", 10)
    # driver.find_element_by_id("com.alibaba.android.rimet:id/login_slide_btn").click()
    driver.find_element_by_name(u"登录").click()
except:
    print("没有登录页面")
    pass
try:
    # 输入账号密码
    driver.wait_activity("com.alibaba.android.rimet:id/et_phone_input", 10)
    driver.find_element_by_id("com.alibaba.android.rimet:id/et_phone_input").send_keys("18062427385")
    driver.find_element_by_id("com.alibaba.android.rimet:id/et_pwd_login").send_keys("123456")
    # 点击登录按钮
    driver.find_element_by_id("com.alibaba.android.rimet:id/btn_next").click()
    # driver.find_element_by_android_uiautomator('new UiSelector().description("同意")').click()
    # driver.find_elements_by_class_name("android.view.View")[231].click()
    time.sleep(3)
    # driver.tap([(1000, 1800)], 10)  # 点击右下角“同意”
except:
    print("Default login")
    pass

# driver.tap([(520, 1800)], 10)
time.sleep(3)
driver.wait_activity("com.alibaba.android.rimet:id/home_bottom_tab_icon_group", 10)
driver.find_elements_by_id("com.alibaba.android.rimet:id/home_bottom_tab_icon_group")[2].click()  # 点击“长江智联”
# print("长江智联进去的页面list：")
# print(driver.contexts)
time.sleep(2)
try:
    driver.wait_activity("考勤打卡", 5)
    driver.find_element_by_android_uiautomator('new UiSelector().description("考勤打卡")').click()
except:
    print("考勤打卡元素找不到，坐标点击")
    # print("考勤打卡进去的页面list：")
    # print(driver.contexts)
    driver.tap([(415, 1067)], 10)  # 点击“考勤打卡”
    pass

# try:
#     # 允许
#     time.sleep(5)
#     driver.wait_activity("ndroid.widget.Button", 5)
#     driver.find_elements_by_class_name("android.widget.Button")[1].click()   # 点击 允许
# except:
#     print("没点击 允许 ")
#     pass

time.sleep(5)
if (t.hour < 10 and t.hour > 7):  # 上班时间
    try:
        driver.wait_activity("上班打卡", 5)
        driver.find_element_by_android_uiautomator('new UiSelector().description("上班打卡")').click()  # 点击上班打卡
        print("*** " + time.strftime("%H:%M:%S", time.localtime()) + " SUCCESS go to work, Manual punch the clock ***")
    except:
        print("上班打卡元素找不到，坐标点击")
        driver.tap([(600, 680)], 10)  # 点击“上班打卡”
        print("*** " + time.strftime("%H:%M:%S", time.localtime()) + " SUCCESS go to work, quickly punch the clock ***")
        pass

    # try:
    #     # 找不到“上班打卡”，显示极速打卡时间
    #     l = driver.find_elements_by_class_name("android.view.View")
    #     for i in range(len(l)):
    #         print(str(i) + ":" + l[i].get_attribute("name"))
    #     # if l[18].get_attribute("name") == "极速打卡":
    #     #     print(l[17].get_attribute("name") + l[18].get_attribute("name"))
    #     #     print("*** " +l[17].get_attribute("name") + " SUCCESS go to work, quickly punch the clock ***")
    #     #  找不到极速打卡，应该是刚急速打卡
    #     else:
    #         print("*** " + time.strftime("%H:%M:%S", time.localtime()) + " SUCCESS go to work, quickly punch the clock ***")
    # except:
    #     pass

elif (t.hour < 18 and t.hour >= 17): # 下班时间
    try:
        driver.wait_activity("下班打卡", 5)
        driver.find_element_by_android_uiautomator('new UiSelector().description("下班打卡")').click()# 点击”下班打卡“
        print("*** " + time.strftime("%H:%M:%S", time.localtime()) + " SUCCESS go off work, Manual punch the clock ***")
    except:
        print("下班打卡元素找不到，坐标点击")
        driver.tap([(538, 1236)], 10)  # 点击“下班打卡”
        print("*** " + time.strftime("%H:%M:%S", time.localtime()) + " SUCCESS go off work, Manual punch the clock ***")
elif (t.hour < 22 and t.hour >= 18): # 下班时间
    try:
        # 点击更新
        driver.wait_activity("更新打卡", 5)
        driver.find_element_by_android_uiautomator('new UiSelector().description("更新打卡")').click()
        driver.wait_activity(u"确定", 5)
        driver.find_element_by_name(u"确定").click()
        print("*** " + time.strftime("%H:%M:%S", time.localtime()) + " SUCCESS go off work, Update punch the clock ***")
    except:
        print("更新打卡元素找不到，坐标点击")
        driver.tap([(167, 1196)], 10)  # 点击“更新打卡”
        driver.wait_activity(u"确定", 5)
        driver.find_element_by_name(u"确定").click()
        print("*** " + time.strftime("%H:%M:%S", time.localtime()) + " SUCCESS go off work, Update punch the clock ***")
        pass
else:
    print("*** No operation ***")
    pass

time.sleep(5)
# 登出
driver.wait_activity("返回", 5)
driver.find_element_by_accessibility_id(u"返回").click()

try:
    driver.find_element_by_accessibility_id(u"返回").click()
except:
    print("***返回成功，准备退出***")
    pass

driver.wait_activity("我的", 5)
driver.find_element_by_name(u"我的").click()
driver.swipe(0, 1622, 0, 530, 500)
driver.find_element_by_id("com.alibaba.android.rimet:id/rl_setting").click()  # 点击 设置
driver.find_element_by_name(u"退出登录").click()
driver.find_element_by_name(u"确认").click()
# 结束
driver.quit()