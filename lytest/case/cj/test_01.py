# coding:utf-8
from selenium import webdriver
import unittest
import time
from selenium.common.exceptions import NoSuchElementException
login_url = "http://59.172.105.83:81/vmsBS/login.jsp"
class TetsLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Ie()
        self.driver.get(login_url)
    def tearDown(self):
        self.driver.quit()
    def test_login(self):
        u'''调用登录类里面的login方法，测试登录用例，元素找不到，抛异常，用例通过'''
        # 调用登录类里面的login方法
        self.driver.find_element_by_class_name("userName").clear()
        self.driver.find_element_by_class_name("userName").send_keys("bsjtest")
        self.driver.find_element_by_class_name("passWord").clear()
        self.driver.find_element_by_class_name("passWord").send_keys("cyl@123456")
        self.driver.find_element_by_class_name("organization").clear()
        self.driver.find_element_by_class_name("organization").send_keys("B00013")

        time.sleep(3)
        # 定位“名字”
        try:
            element = self.driver.find_element("id", "lnk_current_userXX")
        except NoSuchElementException as msg:
            print u"查找元素异常%s"%msg
        # 点击该元素
        else:
            element.click()

if __name__ == "__main__":
    unittest.main()