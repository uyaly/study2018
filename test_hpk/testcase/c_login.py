# coding:utf-8
import unittest
import ddt
from selenium import webdriver
from utils.config import Config, DRIVER_PATH
from utils.log import logger
from pageobject.login import LoginPage


@ddt.ddt
class Login(unittest.TestCase):
    u'''登录'''

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = Config().get('URL')
        self.driver.implicitly_wait(30)
        # self.login = LoginPage(self.driver)  # login参数是LoginPage的实例

    def test_login_case(self):
        # 清除当前的输入
        # self.login.input_username(self.username)
        # self.login.input_password(self.psw)
        # self.login.click_submit()
        self.driver.execute_script("$('#txtaccount').val('')")
        self.driver.execute_script("$('#txtpassword').val('')")
        # 输入用户名和密码，进行登录
        self.driver.execute_script("$('#txtaccount').val(self.username)")
        self.driver.execute_script("$('#txtpassword').val(self.psw)")
        self.driver.execute_script("$('#btlogin').click()")
        # 第4步：测试结果,判断是否登录成功
        result = self.login.is_text_in_element(("id", "loginOut"), "退出")
        # 第5步：期望结果
        expect_result = expect
        self.assertEqual(result, expect_result)
        # links = self.driver.find_elements(*self.locator_result)
        # for link in links:
        #     logger.info(link.text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
