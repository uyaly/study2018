# coding:utf-8
import unittest
class Test(unittest.TestCase):

    @unittest.skip(u"无条件跳过此用例")
    def test_1(self):
        print "测试1"

    @unittest.skipIf(True, u"为True的时候跳过")
    def test_2(self):
        print "测试2"

    @unittest.skipUnless(False, u"为False的时候跳过")
    def test_3(self):
        print "测试3"

    @unittest.expectedFailure
    def test_4(self):
        print "测试4-0"
        self.assertEqual(2, 4, msg=u"判断相等")
        print "测试4-1"

if __name__ == "__main__":
    unittest.main()
