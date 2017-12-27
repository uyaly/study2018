# coding:utf-8
from appium import webdriver
import time
desired_caps = {'platformName': 'Android',
                'deviceName': '11642f40',
                'platformVersion': '6.0',
                'appPackage': 'com.baidu.yuedu',
                'appActivity': 'com.baidu.yuedu.splash.SplashActivity'}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(10)
# 点图书按钮
driver.find_element_by_id("com.baidu.yuedu:id/iv_booktitle").click()
time.sleep(5)
# 切换到图书界面后获取所有的环境
contexts = driver.contexts
print contexts
# 切换到webview
time.sleep(3)
driver.switch_to.context(contexts[1])
now = driver.current_context
print now

# for i in range(len(contexts)):
#     print "循环"+ str(i)
#     print contexts[i]
# driver.switch_to.context(contexts[1])
# driver.switch_to.context(u'WEBVIEW_com.baidu.yuedu')
#     driver.switch_to.context(contexts[i])
# # 获取当前的环境，看是否切换成功
#     now = driver.current_context
#     print now
#     i = i+1
# 切回native
# driver.switch_to.context(contexts[0])
# driver.switch_to.context(u"NATIVE_APP") # 这样也是可以的
# 获取当前的环境，看是否切换成功
# now = driver.current_context
# print now
driver.quit()