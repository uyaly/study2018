# coding:utf-8
import time
import unittest
import ddt
# from selenium.webdriver.common.by import by
from selenium import webdriver
from utils.config import Config, DRIVER_PATH

@ddt.ddt
class login(unittest.TestCase):
    u'''登录'''
    url = Config().get('URL')

    def setUp(self):
        self.driver = webdriver.Firefox()

        self.driver.get(self.url)
        self.driver.implicitly_wait(30)

    def login(self, username, psw):
        # 清除当前的输入
        self.driver.find_element_by_id("txtaccount").clear()
        self.driver.find_element_by_id('txtpassword').clear()
        # 输入用户名和密码，进行登录
        self.driver.find_element_by_id('txtaccount').send_keys("kaka")
        self.driver.find_element_by_id('txtpassword').send_keys("a123")
        self.driver.find_element_by_id('btlogin').click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()