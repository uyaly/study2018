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
                'appPackage': 'com.heyi.oa.onlyoa',
                # apk的launcherActivity
                'appActivity': 'com.heyi.oa.view.SplashActivity',
                # unicodeKeyboard是使用unicode编码方式发送字符串
                'unicodeKeyboard': True,
                # resetKeyboard是将键盘隐藏起来
                'resetKeyboard': True
                }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(5)
try:
    # 输入账号密码
    driver.wait_activity("com.heyi.oa.onlyoa:id/et_input_phone", 5)
    driver.find_element_by_id("com.heyi.oa.onlyoa:id/et_input_phone").clear()
    driver.find_element_by_id("com.heyi.oa.onlyoa:id/et_input_phone").send_keys("wangliang")
    driver.find_element_by_id("com.heyi.oa.onlyoa:id/et_input_password").clear()
    driver.find_element_by_id("com.heyi.oa.onlyoa:id/et_input_password").send_keys("1")
    # 点击登录按钮
    driver.find_element_by_id("com.heyi.oa.onlyoa:id/tv_login_button").click()
except:
    print("Default login")
    pass

time.sleep(3)
# l = driver.find_elements_by_class_name("android.widget.TextView")
# for i in range(len(l)):
#      print(str(i) + ":" + l[i].text)
driver.find_elements_by_class_name("android.widget.TextView")[20].click()  # 点击“工作” ，list类型 [270,1770][540,1920]
# time.sleep(2)
# try:
#     driver.wait_activity("考勤打卡", 5)
#     driver.find_element_by_name("考勤打卡").click()
# except:
#     print("考勤打卡元素找不到，坐标点击")
#     driver.tap([(168, 1008)], 10)  # 点击“考勤打卡” [45,857][292,1160]
#     pass

# time.sleep(5)
# if (t.hour < 10 and t.hour > 7):  # 上班时间
#     try:
#         driver.wait_activity("上班打卡", 5)
#         driver.find_element_by_name("上班打卡").click() # 点击上班打卡
#         print("*** " + time.strftime("%H:%M:%S", time.localtime()) + " SUCCESS go to work, Manual punch the clock ***")
#     except:
#         print("上班打卡元素找不到，坐标点击")
#         # driver.tap([(600, 680)], 10)  # 点击“上班打卡”
#         print("*** " + time.strftime("%H:%M:%S", time.localtime()) + " SUCCESS go to work, quickly punch the clock ***")
#         pass
#
# elif (t.hour <= 18 and t.hour > 17): # 下班时间
#     try:
#         driver.wait_activity("下班打卡", 5)
#         driver.find_element_by_name("下班打卡").click()# 点击”下班打卡“
#         print("*** " + time.strftime("%H:%M:%S", time.localtime()) + " SUCCESS go off work, Manual punch the clock ***")
#     except:
#         print("下班打卡元素找不到，坐标点击")
#         driver.tap([(538, 1236)], 10)  # 点击“下班打卡” [452,1127][668,1200]
#         print("*** " + time.strftime("%H:%M:%S", time.localtime()) + " SUCCESS go off work, Manual punch the clock ***")
# else:
#     print("*** No operation ***")
#     pass

# time.sleep(2)
# # 登出
# driver.wait_activity("返回", 5)
# driver.find_element_by_accessibility_id(u"返回").click()
#
# try:
#     driver.find_element_by_accessibility_id(u"返回").click()
# except:
#     print("***返回成功，准备退出***")
#     pass
#
# driver.wait_activity("我的", 5)
# driver.find_element_by_name(u"我的").click()
# driver.swipe(0, 1622, 0, 530, 500)
# driver.find_element_by_id("com.alibaba.android.rimet:id/rl_setting").click()  # 点击 设置
# driver.find_element_by_name(u"退出登录").click()
# driver.find_element_by_name(u"确认").click()
# 结束
# driver.quit()