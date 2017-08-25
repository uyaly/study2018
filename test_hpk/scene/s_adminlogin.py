# coding:utf-8
import unittest
from utils.config import Config
from selenium import webdriver
from testcase.c_login import login

class adminlogin(unittest.TestCase):
    '''管理员登录场景'''
    login = login()

    def test01(self):
        self.url = Config().get('URL')
        self.username = Config().get('ADMIN')
        self.psw = Config().get('PASSWORD')
        # self.login= login(self)      # login参数是LoginPage的实例
        self.login.login_case(self.username, self.psw, '')


if __name__ == "__main__":
    unittest.main()
