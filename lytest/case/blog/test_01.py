# coding:utf-8
from selenium import webdriver
import unittest
from login_pub import Login_Blog
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
        # self.driver.find_element()
        # 后面接着的操作省略了
if __name__ == "__main__":
    unittest.main()