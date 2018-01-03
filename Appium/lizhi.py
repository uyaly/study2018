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
                'appPackage': 'com.yibasan.lizhifm',
                # apk的launcherActivity
                'appActivity': 'com.yibasan.lizhifm.activities.EntryPointActivity'
                }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# 休眠15秒等待页面加载完成
time.sleep(10)
# button = driver.find_elements_by_class_name("android.widget.LinearLayout")
driver.find_element_by_id("com.yibasan.lizhifm:id/header_user_icon").click()
driver.find_element_by_id("com.yibasan.lizhifm:id/followLabel").click()
driver.find_element_by_id("com.yibasan.lizhifm:id/user_fans_user_head").click()
# android.widget.TextView
# 点击【声音】
driver.find_elements_by_class_name("android.widget.TextView")[11].click()
# 点击【下载】
download = driver.find_element_by_id("com.yibasan.lizhifm:id/btn_download")
download.click()
# 找未下载项，提取标题
tittle = driver.find_elements_by_id("com.yibasan.lizhifm:id/simple_program_item_text_name")
# radio = driver.find_elements_by_id("com.yibasan.lizhifm:id/view_select_status")
for i in range(len(tittle)):
    print tittle[i].text
    tittle[i].click()
    # 点击【开始下载】
    driver.find_element_by_id("com.yibasan.lizhifm:id/download_pop_window_done_layout").click()
    time.sleep(2)
    try:
        download.click()
        print tittle[i].text
    # 执行xx1xx的点击动作，元素没有，会报错.如果元素存在则说明也不会发生
    except:
        # print "第" + str(i+1) + "行未下载"
        pass
    i = i+1

    # 点击【全选】
# driver.find_element_by_id("com.yibasan.lizhifm:id/view_select_all").click()
driver.quit()