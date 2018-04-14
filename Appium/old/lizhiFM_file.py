# coding:utf-8
# !/usr/bin/env Python
from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction
# 前提是小米的安卓手机安装荔枝登录uyaly用户，用到荔枝FM和小米的文件管理两个APP
from screensize import swipeUpLiZhi
import sys
reload(sys)
sys.setdefaultencoding('utf8')

titles = []
titleAll = []

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
driver.find_element_by_id("com.yibasan.lizhifm:id/header_user_icon").click()
driver.find_element_by_id("com.yibasan.lizhifm:id/followLabel").click()
driver.find_element_by_id("com.yibasan.lizhifm:id/user_fans_user_head").click()
# 点击进入【声音】
driver.find_elements_by_class_name("android.widget.TextView")[11].click()
# 点击进入【下载】
download = driver.find_element_by_id("com.yibasan.lizhifm:id/btn_download")
download.click()
# 找未下载项，提取标题
tittle = driver.find_elements_by_id("com.yibasan.lizhifm:id/simple_program_item_text_name")
l = 0
for j in range(7):
    if j % 7 == 0 and j != 0:
        swipeUpLiZhi(driver, n=2)
        l = l+1
    # t = tittle[j-7*l]
    tittle[j-7*l].click()
    # 点击【开始下载】
    driver.find_element_by_id("com.yibasan.lizhifm:id/download_pop_window_done_layout").click()
    try:
    # 如果开始下载会返回，download可以点击，再次进入下载列表，记录标题；
    # 否则抛异常，什么都做继续for循环
        download.click()
        titles.append(tittle[j-7*l].text)
        print "第" + str(j+1) + "行已下载:" + (tittle[j-7*l].text)
        # time.sleep(2)
        # 执行xx1xx的点击动作，元素没有，会报错.如果元素存在则说明也不会发生
    except:
        if tittle[j-7*l].text in titleAll and tittle[j-7*l].text is not "":
            print "第" + str(j+1) + "行本次已重复:" + tittle[j-7*l].text
        else:
            titleAll.append(tittle[j-7*l].text)
            print "第" + str(j+1) + "行未下载:" + (tittle[j-7*l].text)
            break   # 遇到第一个未下载项，跳出for循环
titles = [i + ".mp3" for i in reversed(titles)]
print titles
# 增加一个正在下载为0的判断
for i in range(0, 60):
    try:
        if driver.find_element_by_name("正在下载(0)").is_displayed():
            # print "正在下载0"
            # 关闭荔枝FM
            driver.quit()
        else:
            print "控件未出现,等待1秒"
            time.sleep(1)
    except:
        pass
driver.quit()
time.sleep(10)
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
# for循环下载的音频文件数量的次数
for i in range(len(titles)):
    # print lists[i].text
    # 找到待改名项
    if lists[i].text.find("_hd.mp3") > 0:
        # 长按
        action1 = TouchAction(driver)
        action1.long_press(lists[i]).wait(10000).perform()
        # 更多-重命名
        driver.find_elements_by_class_name("android.widget.Button")[6].click()
        driver.find_element_by_name("重命名").click()
        driver.find_element_by_id("com.android.fileexplorer:id/text").clear()
        driver.find_element_by_id("com.android.fileexplorer:id/text").send_keys(titles[i])
        driver.find_element_by_name("确定").click()
time.sleep(5)
driver.quit()