# coding:utf-8
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://bj.ganji.com/")
driver.implicitly_wait(10)
# 获取当前窗口句柄
h = driver.current_window_handle
print (h)   # 打印首页句柄
driver.find_element_by_link_text("北京招聘").click()
all_h = driver.window_handles
print(all_h)   # 打印所有句柄
# 方法一：判断句柄，不等于首页就切换
# for i in all_h:
#     if i != h:
#         driver.switch_to.window(i)
#         print driver.title
# 方法二：获取list里面第二个直接切换
driver.switch_to.window(all_h[1])
print(driver.title)

# 关闭新窗口
driver.close()
# 切换到首页句柄
driver.switch_to.window(h)
# 打印当前的title
print(driver.title)
