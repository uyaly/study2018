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
                'appPackage': 'com.android.fileexplorer',
                # apk的launcherActivity
                'appActivity': 'com.android.fileexplorer.FileExplorerTabActivity'
                }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
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
    print lists[i].text
    if lists[i].text.find("_sd.m4a") > 0:
        driver.tap([(176, 543), (889, 601)], 3500)
        driver.find_element_by_name("更多").click()
        driver.find_element_by_name("重命名").click()
        driver.find_element_by_id("com.android.fileexplorer:id/text").send_keys("Day160K.The name of the story is《Homes》解释")

time.sleep(5)
driver.quit()