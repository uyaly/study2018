# coding:utf-8
from selenium import webdriver
import unittest
import time
from selenium.common.exceptions import NoSuchElementException
login_url = "http://59.172.105.83:81/vmsBS/login.jsp"
class TetsLogin(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Ie()
        self.driver = webdriver.Firefox()
        self.driver.get(login_url)

    def test_login(self):
        u'''调用登录类里面的login方法，测试登录用例，元素找不到，抛异常，用例通过'''
        # 调用登录类里面的login方法
        time.sleep(3)
        self.driver.find_element_by_xpath(".//*[@id='loginForm']/div[1]/input").send_keys("bsjtest")

        self.driver.find_element_by_xpath(".//*[@id='loginForm']/div[2]/input").clear()
        self.driver.find_element_by_xpath(".//*[@id='loginForm']/div[2]/input").send_keys("cyl@123456")

        self.driver.find_element_by_xpath(".//*[@id='loginForm']/div[3]/input").clear()
        self.driver.find_element_by_xpath(".//*[@id='loginForm']/div[3]/input").send_keys("B00013")

        self.driver.find_element_by_class_name("login_btn").click()

        time.sleep(3)
        # 定位“退出”
        try:
            element = self.driver.find_element("id", "exitSys")
        except NoSuchElementException as msg:
            print u"查找元素异常%s"%msg
        # 点击该元素
        else:
            # element.click()
            print "登录成功！"

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()