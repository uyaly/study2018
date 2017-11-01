# coding:utf-8
from selenium import webdriver
import unittest
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
login_url = "http://59.172.105.83:81/vmsBS/login.jsp"


class TestLogin(unittest.TestCase):

    @classmethod
    def setUp(cls):
        # cls.driver = webdriver.Ie()  # 真心找不到元素，不知道原因
        cls.driver = webdriver.Firefox()
        # cls.driver = webdriver.Chrome()
        cls.driver.get(login_url)
        cls.driver.maximize_window()

    def test_login(self):
        WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath(".//*[@id='loginForm']/div[1]/input")).send_keys("")
        self.driver.find_element_by_xpath(".//*[@id='loginForm']/div[1]/input").send_keys("bsjtest")

        self.driver.find_element_by_xpath(".//*[@id='loginForm']/div[2]/input").clear()
        self.driver.find_element_by_xpath(".//*[@id='loginForm']/div[2]/input").send_keys("cyl@123456")

        self.driver.find_element_by_xpath(".//*[@id='loginForm']/div[3]/input").clear()
        self.driver.find_element_by_xpath(".//*[@id='loginForm']/div[3]/input").send_keys("B00013")

        self.driver.find_element("class name", "login_btn").click()

        # 定位“退出”
        # try:
        #     WebDriverWait(self.driver, 5).until(lambda x: x.find_element("id", "exitSys"))
        #     # element = self.driver.find_element("id", "exitSys")
        # except NoSuchElementException as msg:
        #     print u"查找元素异常%s"%msg
        # # 点击该元素
        # else:
        #     # element.click()
        #     print "登录成功！"
        frame1 = self.driver.find_element("id", "iframe_1")
        self.driver.switch_to.frame(frame1)
        # 进入指令管理
        self.driver.find_elements("class name", "panel-title")[4].click()
        self.driver.find_element_by_link_text("指令管理").click()
        self.driver.switch_to.default_content()
        # 输入车牌
        # self.driver.find_element("class name","validatebox-text").send_keys(u"鄂A0001")
        # self.driver.find_element_by_css_selector("input.combo-text").send_keys("鄂A0001")
        # self.driver.find_element_by_xpath(".//*[@id='VsearchBar']/div[2]/span/input[1]").send_keys("Keys.ENTER")
        # self.driver.find_element("id", "_easyui_tree_8").click()
        self.driver.find_element_by_xpath(".//*[@id='_easyui_tree_11']/span[4]").click()
        # a = self.driver.find_elements("class name", "tree-checkbox")
        # 进入拍照
        self.driver.find_element_by_xpath(".//*[@id='_easyui_tree_6']/span[3]").click()
        self.driver.find_element_by_xpath(".//*[@id='_easyui_tree_21']/span[4]").click()
        self.driver.find_element_by_xpath(".//*[@id='_easyui_tree_32']/span[5]").click()
        # 拍照参数设置
        self.driver.find_element("id", "photograph_num").send_keys("1")
        self.driver.find_element("id", "photograph_time").send_keys("0")
        self.driver.find_element("class name", "l-btn-left").click()

    # def test_takephoto(self):

    # @classmethod
    # def tearDown(cls):
    #     cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)