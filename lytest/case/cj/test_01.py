# coding:utf-8
from selenium import webdriver
import unittest
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
login_url = "http://59.172.105.83:81/vmsBS/login.jsp"
class TetsLogin(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Ie()  # 真心找不到元素，不知道原因
        # self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
        self.driver.get(login_url)
        self.driver.maximize_window()

    def test_login(self):
        WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath(".//*[@id='loginForm']/div[1]/input")).send_keys("")
        self.driver.find_element_by_xpath(".//*[@id='loginForm']/div[1]/input").send_keys("bsjtest")

        self.driver.find_element_by_xpath(".//*[@id='loginForm']/div[2]/input").clear()
        self.driver.find_element_by_xpath(".//*[@id='loginForm']/div[2]/input").send_keys("cyl@123456")

        self.driver.find_element_by_xpath(".//*[@id='loginForm']/div[3]/input").clear()
        self.driver.find_element_by_xpath(".//*[@id='loginForm']/div[3]/input").send_keys("B00013")

        self.driver.find_element("class name","login_btn").click()

        # 定位“退出”
        try:
            WebDriverWait(self.driver, 5).until(lambda x: x.find_element("id", "exitSys"))
            # element = self.driver.find_element("id", "exitSys")
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