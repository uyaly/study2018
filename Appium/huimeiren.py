# coding:utf-8
from appium import webdriver
import datetime
import time
import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
t = datetime.datetime.now()
desired_caps = {
                # 这里是声明android还是ios的环境
                'platformName': 'Android',
                # 手机设备名称，通过adb devices查看
                # 'deviceName': '11642f40', # 自己的小米4
                'deviceName': 'cc2ae2f4', # 测试机小米4
                # 'deviceName': 'ed278f80', # 测试机小米4
                # android系统的版本号
                'platformVersion': '7.0',
                # apk包名
                #
                'appPackage': 'com.heyi.oa.onlyoa',
                # apk的launcherActivity
                'appActivity': 'com.heyi.oa.view.SplashActivity',
                # 'automationName': 'uiautomator2',
                # 'unicodeKeyboard':True,#绕过手机键盘操作，unicodeKeyboard是使用unicode编码方式发送字符串
                # 'resetKeyboard':True,#绕过手机键盘操作，resetKeyboard是将键盘隐藏起来
                }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 处理滑动引导页
# width = driver.manage().window().getSize().width
# height = driver.manage().window().getSize().height
width = driver.get_window_size()['width']
height = driver.get_window_size()['height']
for i in range(0,3):
    driver.swipe(width * 3 / 4, height / 2, width / 4, height / 2, 500)
    time.sleep(3)

# 定位'立即体验'入口
try:
    driver.find_element_by_id("com.heyi.oa.onlyoa:id/tv_to_login").click()
except:
    print('没有定位到立即体验入口！')





# sleep(10)
# cur_activity = driver.current_activity#获取当前Activity
# print(cur_activity)#输出.base.ui.MainActivity

# time.sleep(5)
try:
    # 进入登录
    driver.wait_activity("com.heyi.oa.onlyoa:id/et_input_phone", 2)
    driver.find_element_by_id("com.heyi.oa.onlyoa:id/et_input_phone").click()
    driver.find_element_by_name(u"登录").click()
except:
    print("没有登录页面")
    pass
try:
    # 输入账号密码
    driver.wait_activity("com.heyi.oa.view.activity.l", 2)
    driver.find_element_by_id("com.heyi.oa.onlyoa:id/et_input_phone").clear()
    driver.find_element_by_id("com.heyi.oa.onlyoa:id/et_input_phone").send_keys("wangliang")
    time.sleep(1)
    driver.find_element_by_id("com.heyi.oa.onlyoa:id/et_input_password").clear()
    driver.find_element_by_id("com.heyi.oa.onlyoa:id/et_input_password").send_keys("1")
    time.sleep(1)
    # 点击登录按钮
    driver.find_element_by_id("com.heyi.oa.onlyoa:id/tv_login_button").click()
    # driver.find_element_by_android_uiautomator('new UiSelector().description("同意")').click()
    # driver.find_elements_by_class_name("android.view.View")[231].click()
    # time.sleep(3)
    # driver.find_element_by_id("com.heyi.oa.onlyoa:id/tv_login_button").click()
    # driver.tap([(1000, 1800)], 10)  # 点击右下角“同意”
except:
    driver.wait_activity("com.heyi.oa.view.activity.login.LoginActivity", 2)
    driver.find_element_by_id("com.heyi.oa.onlyoa:id/tv_login_button").click()
    print("Default login success ！")
    pass

# driver.tap([(520, 1800)], 10)
time.sleep(2)
driver.wait_activity("com.heyi.oa.view.MainActivi", 2)
driver.find_elements_by_id("com.heyi.oa.onlyoa:id/icon")[1].click()  # 点击“工作” ，list类型
time.sleep(2)
driver.find_elements_by_id("com.heyi.oa.onlyoa:id/iv_icon")[0].click() #点击‘考勤打卡’，list类型
# print("长江智联进去的页面list：")
# print(driver.contexts)
time.sleep(2)
try:
    driver.wait_activity("com.heyi.oa.view.activity.word.newIntelligence.AttendanceClockActivityNew", 2)
    # driver.find_element_by_android_uiautomator('new UiSelector().description("考勤打卡")').click()
except:
    print("考勤打卡元素找不到，进不去，经纬度点击进入")
    # print("考勤打卡进去的页面list：")
    # print(driver.contexts)
    # driver.tap([(415, 1067)], 10)  # 点击“考勤打卡”
    pass

# try:
#     # 允许
#     time.sleep(5)
#     driver.wait_activity("ndroid.widget.Button", 5)
#     driver.find_elements_by_class_name("android.widget.Button")[1].click()   # 点击 允许
# except:
#     print("没点击 允许 ")
#     pass

# time.sleep(10)
# if (t.hour < 10 and t.hour > 7):  # 上班时间
#     try:
#         driver.wait_activity("com.heyi.oa.view.activity.word.newIntelligence.AttendanceClockActivityNew", 2)
#         driver.find_elements_by_name(u"上班打卡").click()  # 点击上班打卡
#         print("*** " + time.strftime("%H:%M:%S", time.localtime()) + " SUCCESS go to work, Manual punch the clock ***")
#     except:
#         print('未定位到上班打卡！')
#         pass
#
#     # try:
#     #     # 找不到“上班打卡”，显示极速打卡时间
#     #     l = driver.find_elements_by_class_name("android.view.View")
#     #     for i in range(len(l)):
#     #         print(str(i) + ":" + l[i].get_attribute("name"))
#     #     # if l[18].get_attribute("name") == "极速打卡":
#     #     #     print(l[17].get_attribute("name") + l[18].get_attribute("name"))
#     #     #     print("*** " +l[17].get_attribute("name") + " SUCCESS go to work, quickly punch the clock ***")
#     #     #  找不到极速打卡，应该是刚急速打卡
#     #     else:
#     #         print("*** " + time.strftime("%H:%M:%S", time.localtime()) + " SUCCESS go to work, quickly punch the clock ***")
#     # except:
#     #     pass
#
# elif (t.hour < 23 and t.hour >= 17): # 下班时间
#     try:
#         # driver.wait_activity("com.heyi.oa.view.activity.word.newIntelligence.AttendanceClockActivityNew", 2)
#         driver.find_elements_by_name(u"下班打卡").click() # 点击”下班打卡“
#         print("*** " + time.strftime("%H:%M:%S", time.localtime()) + " SUCCESS go off work, Manual punch the clock ***")
#     except:
#         print('未定位到下班打卡')
#         # 找不到“下班打卡“，点击更新
#         # driver.wait_activity("更新打卡", 5)
#         # driver.find_element_by_android_uiautomator('new UiSelector().description("更新打卡")').click()
#         # driver.wait_activity(u"确定", 5)
#         # driver.find_element_by_name(u"确定").click()
#         # print("*** " + time.strftime("%H:%M:%S", time.localtime()) + " SUCCESS go off work, Update punch the clock ***")
#         pass
# else:
#     print("*** No operation ***")
#     pass
#
# time.sleep(5)
# # 登出
# # driver.wait_activity("返回", 5)
# driver.find_element_by_id("com.heyi.oa.onlyoa:id/iv_back").click() # 返回
#
# # try:
# #     driver.find_element_by_accessibility_id(u"返回").click()
# # except:
# #     print("***返回成功，准备退出***")
# #     pass
#
# # try:
# #     # driver.wait_activity("com.heyi.oa.view.MainActivity", 5) #进入我的页面
# #     driver.find_elements_by_id("com.heyi.oa.onlyoa:id/icon")[3].click()
# #     # driver.find_element_by_name(u"我的").click()
# #     time.sleep(2)
# #     driver.find_elements_by_id("com.heyi.oa.onlyoa:id/iv_setting").click()
# # except:
# #     print('未找到我的页面！')
#
# # time.sleep(3)
# # # driver.find_elements_by_id("com.heyi.oa.onlyoa:id/iv_setting")[3].click() #进入设置页面
# # driver.wait_activity("com.heyi.oa.view.activity.mine.newMine.settings.SettingsActivity", 2)  # 进入设置页面
# # driver.find_element_by_id("com.heyi.oa.onlyoa:id/bt_logout").click() #点击退出登录
# # print('登出成功！')
#
# # driver.swipe(0, 1622, 0, 530, 500)
# # driver.find_element_by_id("com.alibaba.android.rimet:id/rl_setting").click()  # 点击 设置
# # driver.find_element_by_name(u"退出登录").click()
# # driver.find_element_by_name(u"确认").click()
# # 结束
# driver.quit()