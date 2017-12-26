# coding:utf-8
from appium import webdriver
import time
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
# 休眠15秒等待页面加载完成
time.sleep(5)
driver.find_element_by_id("com.alibaba.android.rimet:id/home_bottom_tab_button_work").click()
# driver.find_elements_by_class_name("android.widget.RelativeLayout")[6].click()
contexts = driver.contexts
print contexts
# 切换到webview
driver.switch_to.context(contexts[1])
# 获取当前的环境，看是否切换成功
now = driver.current_context
print now

# 切回native
# driver.switch_to.context(contexts[0])
driver.switch_to.context("NATIVE_APP") # 这样也是可以的
# 获取当前的环境，看是否切换成功
now1 = driver.current_context
print now1

driver.quit()