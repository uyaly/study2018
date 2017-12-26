# coding:utf-8
# 引入WebDriver包
from selenium import webdriver
# 引入WebDriver Keys包
from selenium.webdriver.common.keys import Keys
import time
# 创建浏览器对象
driver = webdriver.Firefox()
# driver = webdriver.Ie()
# driver = webdriver.Chrome()

# 导航主页
driver.get('http://www.coyia.com.tw:8019/Default/Login')
# 休眠3秒
time.sleep(3)
# 隐式等待3秒
driver.implicitly_wait(10)
# 检查标题
assert '轰扑克皇家俱乐部' in driver.title
# 页面刷新
driver.refresh()
# 返回上一页
driver.back()
# 切换到下一页
driver.forward()
# 设置窗口大小
driver.set_window_size(540,960)
# 窗口最大化
driver.maximize_window()
# 截屏
driver.get_screenshot_as_file("d:\\3.jpg")
# 找到
# driver.find_element_by_id('txtaccounttext').send_keys("kaka")
# driver.find_element_by_id('txtpasswordtext').send_keys("a123")
#
# driver.find_element_by_id('btlogin').click()
# driver.find_element_by_link_text('帐号管理').click()
# driver.find_element_by_link_text('公司').click()
# 关闭浏览器
driver.quit()