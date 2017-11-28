# coding:utf-8
import unittest
from selenium import webdriver

class Login_test(unittest.TestCase):
    u'''登录页面的case'''
    # def setUp(AutoSentChatroom):
        # AutoSentChatroom.driver = webdriver.Firefox()
        # AutoSentChatroom.driver.get("http://47.52.77.154:8015/Default/Login")

    def test_case(self):
        '''登录用例的方法,'''
        company = [11,22,33,44,55]
        print len(company)
        print company[0]
        i = 0
        for i in xrange(len(company)):
            print company[i]
if __name__ == "__main__":
    unittest.main()