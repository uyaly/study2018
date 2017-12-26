# coding:utf-8
from selenium import webdriver

driver = webdriver.Firefox()


# 截图功能
def get_screen():
    '''截图'''
    import time
    nowTime = time.strftime("%Y_%m_%d_%H_%M_%S")
    driver.get_screenshot_as_file('%s.jpg' % nowTime)


# 自动截图装饰器
def screen(func):
    '''截图装饰器'''

    def inner(*args, **kwargs):3
        try:
            f = func(*args, **kwargs)
            return f
        except:
            get_screen()  # 失败后截图
            raise

    return inner


@screen
def search(driver):
    driver.get("https://www.baidu.com")
    driver.find_element_by_id("kw11").send_keys("python")  # 此行运行失败的
    driver.find_element_by_id("su").click()


search(driver)  # 执行search
