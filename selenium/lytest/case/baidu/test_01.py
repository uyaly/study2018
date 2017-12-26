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
        u'''测试登录用例，账号：xx 密码xx'''
        print "执行测试用例01"
    def test03(self):
        u'''测试登搜索用例，关键词：xxx'''
        print "执行测试用例03"
    def test02(self):
        print "执行测试用例02"

if __name__ == "__main__":
    unittest.main()