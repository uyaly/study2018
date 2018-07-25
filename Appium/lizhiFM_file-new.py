# coding:utf-8
# !/usr/bin/env Python
from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction
# 前提是小米的安卓手机安装荔枝登录uyaly用户，用到荔枝FM和小米的文件管理两个APP
# 问题是只能下载首页未下载项
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
try:
    driver.wait_activity("允许", 5)
    # 允许
    driver.find_element_by_name("允许").click()
except:
    pass
# 点击头像
try:
    driver.wait_activity("com.yibasan.lizhifm:id/header_user_icon", 1)
    driver.find_element_by_id("com.yibasan.lizhifm:id/header_user_icon").click()
except:
    driver.wait_activity("com.yibasan.lizhifm:id/header_no_user", 1)
    driver.find_element_by_id("com.yibasan.lizhifm:id/header_no_user").click()
    # 手机登录
    driver.find_element_by_id("com.yibasan.lizhifm:id/login_by_phone").click()
    driver.tap([(500, 349), (984, 511)], 500)
    time.sleep(5)
    driver.tap([(210, 1300)], 10)  # 1
    driver.tap([(440, 1600)], 10)  # 8
    driver.tap([(440, 1800)], 10)  # 0
    driver.tap([(700, 1500)], 10)  # 6
    driver.tap([(500, 1300)], 10)  # 2
    driver.tap([(210, 1500)], 10)  # 4
    driver.tap([(500, 1300)], 10)  # 2
    driver.tap([(210, 1600)], 10)  # 7
    driver.tap([(800, 1300)], 10)  # 3
    driver.tap([(440, 1600)], 10)  # 8
    driver.tap([(440, 1500)], 10)  # 5
    driver.find_element_by_name("确认").click()

    # 输入密码
    driver.wait_activity("com.yibasan.lizhifm:id/edit_text", 1)
    driver.find_element_by_id("com.yibasan.lizhifm:id/edit_text").send_keys("612101010")
    driver.find_element_by_name("登录").click()
    # 点击头像
    driver.wait_activity("com.yibasan.lizhifm:id/header_user_icon", 2)
    driver.find_element_by_id("com.yibasan.lizhifm:id/header_user_icon").click()
    pass
driver.wait_activity("com.yibasan.lizhifm:id/followLabel", 10)
# 关注
driver.find_element_by_id("com.yibasan.lizhifm:id/followLabel").click()
driver.find_element_by_id("com.yibasan.lizhifm:id/user_fans_user_head").click()
# 点击进入【声音】
driver.find_elements_by_class_name("android.widget.TextView")[11].click()
# 点击进入【下载】
download = driver.find_element_by_id("com.yibasan.lizhifm:id/btn_download")
download.click()
# # # 全选
# # driver.find_elements_by_id("com.yibasan.lizhifm:id/view_select_all")
#
# 找未下载项，提取标题
tittle = driver.find_elements_by_id("com.yibasan.lizhifm:id/simple_program_item_text_name")
# for j in range(len(tittle)):
for j in range(2):
    # 点击标题
    tittle[j].click()
    # 开始下载
    driver.find_element_by_id("com.yibasan.lizhifm:id/download_pop_window_done_layout").click()
    try:
        # 如果开始下载会返回，download可以点击，再次进入下载列表，记录标题；
        # 否则抛异常，什么都做继续for循环
            download.click()
            titles.append(tittle[j].text)
            print "*** " + str(j+1) + " line has been downloaded:" + (tittle[j].text) + " ***"
    # 执行xx1xx的点击动作，元素没有，会报错.如果元素存在则说明也不会发生
    except:
        # print str(j+1) + "is not downloaded:" + (tittle[j].text)
        break   # 遇到第一个未下载项，跳出for循环
titles = [i + ".mp3" for i in reversed(titles)]
# print titles
# 等待下载完毕，等60秒
driver.wait_activity(u"正在下载(0)", 60)
driver.quit()
# 增加一个正在下载为0的判断
# for i in range(0, 60):
#     try:
#         if driver.find_element_by_name(u"正在下载(0)").is_displayed():
#             # print "正在下载0"
#             # 关闭荔枝FM
#             driver.quit()
#         else:
#             # print u"控件未出现,等待1秒"
#             time.sleep(1)
#     except:
#         pass


if titles != []:
    time.sleep(5)
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
            action1.long_press(lists[i]).wait(1000).perform()
            # 更多-重命名
            driver.find_elements_by_class_name("android.widget.Button")[6].click()
            driver.find_element_by_name("重命名").click()
            driver.find_element_by_id("com.android.fileexplorer:id/text").clear()
            driver.find_element_by_id("com.android.fileexplorer:id/text").send_keys(titles[i])
            driver.find_element_by_name("确定").click()
    time.sleep(5)
    driver.quit()
else:
    print("*** 0 files have been downloaded ***")