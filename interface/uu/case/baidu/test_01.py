# coding:utf-8
import unittest
import time
class Test(unittest.TestCase):
    def setUp(self):
        print "start!"
    def tearDown(self):
        time.sleep(1)
        print "end!"
    def test01(self):
        u'''测试登录用例，账号：XX 密码 xx'''
        print "执行测试用例01"
    def test02(self):
        u'''测试登搜索用例，关键词：xxx'''
        print "执行测试用例02"