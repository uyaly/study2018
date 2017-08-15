# coding:utf-8
from selenium import webdriver
import unittest
from login_pub import Login_Blog
import time
from selenium.common.exceptions import NoSuchElementException
login_url = "https://passport.cnblogs.com/user/signin"
class TetsLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(login_url)
    def tearDown(self):
        self.driver.quit()
    def test_login(self):
        # 调用登录类里面的login方法
        Login_Blog(self.driver).login("uyaly", "ly612101010!")
        time.sleep(3)
        # 定位“名字”
        try:
            element = self.driver.find_element("id", "lnk_current_user_")
        except NoSuchElementException as msg:
            print u"查找元素异常%s"%msg
        # 点击该元素
        else:
            element.click()

if __name__ == "__main__":
    unittest.main()