# coding:utf-8
from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction



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
# 获得机器屏幕大小x,y
def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)
# 屏幕向上滑动
def swipeUp(t):
    l = getSize()
    x1 = int(l[0] * 0.5)  #x坐标
    y1 = int(l[1] * 0.75)   #起始y坐标
    y2 = int(l[1] * 0.25)   #终点y坐标
    driver.swipe(x1, y1, x1, y2,t)
# 屏幕向下滑动
def swipeDown(t):
    l = getSize()
    x1 = int(l[0] * 0.5)  #x坐标
    y1 = int(l[1] * 0.25)   #起始y坐标
    y2 = int(l[1] * 0.75)   #终点y坐标
    driver.swipe(x1, y1, x1, y2,t)

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
# 找标题项，提取标题
for k in range(3):
    titles = driver.find_elements_by_id("com.yibasan.lizhifm:id/simple_program_item_text_name")
    # 调用向下滑动
    swipeUp(2000)
    # titles = []
    titles.append(titles)

for i in range(len(titles)):
    print titles[i].text
    # ac = driver.current_activity
    # print(ac)
    # .activities.fm.ChoiceUserVoiceDownloadActivity
    # 增加一个正在下载为0的判断
    # if driver.find_element(id, "com.yibasan.lizhifm:id/txt_downloading_count_title").is_displayed():
# try:
#     if driver.find_element_by_name("正在下载(0)").is_displayed():
#         print "正在下载0"
#         driver.quit()
#     else:
#         print "控件未出现"
# except:
#     pass


    # tittle[i].click()
    # # 点击【开始下载】
    # driver.find_element_by_id("com.yibasan.lizhifm:id/download_pop_window_done_layout").click()
    # time.sleep(2)
    # try:
    #     download.click()
    #     print tittle[i].text
    # # 执行xx1xx的点击动作，元素没有，会报错.如果元素存在则说明也不会发生
    # except:
    #     # print "第" + str(i+1) + "行未下载"
    #     pass

    # 点击【全选】
# driver.find_element_by_id("com.yibasan.lizhifm:id/view_select_all").click()
driver.quit()