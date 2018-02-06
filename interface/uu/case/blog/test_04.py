# coding:utf-8
import unittest
from selenium import webdriver

class Test1(unittest.TestCase):
    def setUp(self):
        print("start!")
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.baidu.com")
        self.driver.implicitly_wait(30)

    def tearDown(self):
        print("end!")
        self.driver.close()

    def test_01(self):
        self.driver.find_element_by_id("kw").send_keys("yoyo")


    def test_02(self):
        self.driver.find_element_by_id("kw").send_keys("haha")

if __name__ == "__main__":
    unittest.main()
