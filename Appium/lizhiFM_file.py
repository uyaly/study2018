# coding:utf-8
# !/usr/bin/env Python

from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction

titles = []
desired_caps1 = {
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

desired_caps2 = {
                # 这里是声明android还是ios的环境
                'platformName': 'Android',
                # 手机设备名称，通过adb devices查看
                'deviceName': '11642f40',
                # android系统的版本号
                'platformVersion': '6.0.1',
                # apk包名
                'appPackage': 'com.android.fileexplorer',
                # apk的launcherActivity
                'appActivity': 'com.android.fileexplorer.FileExplorerTabActivity',
                # unicodeKeyboard是使用unicode编码方式发送字符串
                'unicodeKeyboard': True,
                # resetKeyboard是将键盘隐藏起来
                'resetKeyboard': True
            }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps1)
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
for n in range(len(tittle)):
    # print tittle[i].text
    tittle[n].click()
    # 点击【开始下载】
    driver.find_element_by_id("com.yibasan.lizhifm:id/download_pop_window_done_layout").click()

    try:
        download.click()
        # print tittle[i].text
        titles.append(tittle[n].text + ".m4a")
        time.sleep(2)
    # 执行xx1xx的点击动作，元素没有，会报错.如果元素存在则说明也不会发生
    except:
        # print "第" + str(i+1) + "行未下载"
        pass
    n = n+1
titles = [i + ".m4a" for i in reversed(titles)]
print titles
driver.quit()
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps2)
# 休眠15秒等待页面加载完成
time.sleep(5)
driver.find_element_by_name("手机").click()
# 排序
driver.find_element_by_id("com.android.fileexplorer:id/more").click()
driver.find_element_by_name("排序").click()
driver.find_element_by_name("名称").click()
# 进目录
driver.find_element_by_name("183").click()
driver.find_element_by_name("LizhiFM").click()
driver.find_element_by_name("Files").click()
driver.find_element_by_name("download").click()
# 列表排序
driver.find_element_by_id("com.android.fileexplorer:id/more").click()
driver.find_element_by_name("排序").click()
driver.find_element_by_name("修改时间").click()

# 长按文件重命名
lists = driver.find_elements_by_id("com.android.fileexplorer:id/file_name")
for i in range(len(lists)):
    # print lists[i].text
    # 找到待改名项
    if lists[i].text.find("_sd.m4a") > 0:
        # 长按
        action1 = TouchAction(driver)
        action1.long_press(lists[i]).wait(10000).perform()
        # 更多-重命名
        driver.find_elements_by_class_name("android.widget.Button")[6].click()
        driver.find_element_by_name("重命名").click()
        driver.find_element_by_id("com.android.fileexplorer:id/text").clear()
        driver.find_element_by_id("com.android.fileexplorer:id/text").send_keys(titles[i])
        driver.find_element_by_name("确定").click()
        i = i+1
time.sleep(5)
driver.quit()