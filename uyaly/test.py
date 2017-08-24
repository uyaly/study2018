# coding:utf-8
import unittest
from ly_selenium import browser
from ly_pageobject import LoginPage, login_url
class Login_test(unittest.TestCase):
    u'''登录页面的case'''
    def setUp(self):
        self.driver = browser()
        self.login= LoginPage(self.driver)      #   login参数是LoginPage的实例
        self.login.open(login_url)
    def login_case(self, username, psw, expect=True):
        '''登录用例的方法,'''
        # 第1步：输入账号
        self.login.input_username(username)
        # 第2步: 输入密码
        self.login.input_password(psw)
        # 第3步：点登录按钮
        self.login.click_submit()
        # 第4步：测试结果,判断是否登录成功
        result = self.login.is_text_in_element(("id","lnk_current_user"),"uyaly")
        # 第5步：期望结果
        expect_result = expect
        self.assertEqual(result, expect_result)
    def test_login01(self):
        u'''输入正确账号密码'''
        self.login_case("uyaly", "ly612101010!", True)
    def test_login02(self):
        u'''输入错误账号密码'''
        self.login_case("xx", "xx", False)
    def tearDown(self):
     self.driver.quit()
if __name__ == "__main__":
    unittest.main()
