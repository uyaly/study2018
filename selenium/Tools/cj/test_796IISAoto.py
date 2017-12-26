# coding:utf-8
from selenium import webdriver
import unittest
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
login_url = "http://59.172.105.83:81/vmsBS/login.jsp"
username = "bsjtest"
password = "cyl@123456"
group = "B00013"
brand = u"鄂AC28U2"

class TestLogin(unittest.TestCase):

    @classmethod
    def setUp(cls):
        # cls.driver = webdriver.Ie()  # 找不到元素，不知道原因
        cls.driver = webdriver.Firefox()
        # cls.driver = webdriver.Chrome()
        cls.driver.get(login_url)
        cls.driver.maximize_window()

    def test_login(self):
        '''登录'''
        WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath(".//*[@id='loginForm']/div[1]/input")).send_keys("")
        self.driver.find_element_by_xpath(".//*[@id='loginForm']/div[1]/input").send_keys(username)
        self.driver.find_element_by_xpath(".//*[@id='loginForm']/div[2]/input").clear()
        self.driver.find_element_by_xpath(".//*[@id='loginForm']/div[2]/input").send_keys(password)
        self.driver.find_element_by_xpath(".//*[@id='loginForm']/div[3]/input").clear()
        self.driver.find_element_by_xpath(".//*[@id='loginForm']/div[3]/input").send_keys(group)
        self.driver.find_element("class name", "login_btn").click()

        # 定位“退出”
        # try:
        #     WebDriverWait(self.driver, 5).until(lambda x: x.find_element("id", "exitSys"))
        # except NoSuchElementException as msg:
        #     print u"查找元素异常%s"%msg
        #
        # else:
        #     # element.click()
        #     print "登录成功！"

    # def test_808(self):
        '''测试部标协议'''
        frame1 = self.driver.find_element("id", "iframe_1")
        self.driver.switch_to.frame(frame1)
        # 进入指令管理
        self.driver.find_elements("class name", "panel-title")[4].click()
        self.driver.find_element_by_link_text("指令管理").click()
        # 切换iframe2
        WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_class_name("sys_main_iframe"))
        frame2 = self.driver.find_element_by_class_name("sys_main_iframe")
        print frame2.text
        self.driver.switch_to.frame(frame2)
        time.sleep(3)
        # 选中测试车辆
        # self.driver.find_element("class name", "combo-text").send_keys(u"鄂A0001")
        # self.driver.find_element("class name", "combo-text").send_keys(Keys.ENTER)
        car = self.driver.find_elements("class name", "tree-title")
        checkbox = self.driver.find_elements("class name", "tree-checkbox")
        i = 0
        for i in range(len(car)):
            # print car[i].text
            if car[i].text == "    "+ brand:
                # print car[i].text + u"找到的车"
                checkbox[i].click()
            i = i+1

        # self.driver.execute_script("$('input.combo-text.validatebox-text').val('ce0')")

        # 选择指令
        # self.driver.find_element("id", "_easyui_tree_6").click()
        # self.driver.find_element("id", "_easyui_tree_21").click()
        # self.driver.find_element("id", "_easyui_tree_32").click()
        # # 拍照参数设置
        # self.driver.find_element("id", "photograph_num").send_keys("1")
        # self.driver.find_element("id", "photograph_time").send_keys("0")
        # self.driver.find_element("class name", "l-btn-left").click()
        # 切回
        self.driver.switch_to.default_content()


    @classmethod
    def tearDown(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)