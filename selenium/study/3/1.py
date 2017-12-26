# coding:utf-8
import unittest
class TestCase(unittest.TestCase):
    # 3 method names begin '3*'
    def testAdd(self):
        self.assertEqual((1 + 2), 3)
        self.assertEqual(0 + 1, 1)
    def testMultiply(self):
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)
    def testminus(self):
        u'''这里是测试减法'''
        self.assertEqual(6-5, 1)
    def testdivide(self):
        u'''这里是测试除法'''
        self.assertEqual(7/2, 3.5)
if __name__ == '__main__':
    unittest.main()