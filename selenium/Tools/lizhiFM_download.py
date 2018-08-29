# coding:utf-8
import sys
import unittest
import ddt
from selenium import webdriver
import time
reload(sys)
sys.setdefaultencoding('utf-8')

@ddt.ddt
class lizhi(unittest.TestCase):
    u'''lizhi'''

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.lizhi.fm/user/2590902823435862060")

    def test01_download(self):
        u'''下载'''
        play = self.driver.find_elements_by_class_name("leftPlayBtn")
        # play = self.driver.find_elements_by_class_name("radio-list-item-index")
        for i in range(len(play)):
            print(play[i].text)
        play[5].click()
        time.sleep(5)

    @classmethod
    def tearDownClass(self):
        # 关闭浏览器
        self.driver.quit()

# 执行测试主函数
if __name__ == '__main__':
    # 执行main全局方法，将会执行上述所有以test开头的测试方法
    unittest.main(verbosity=2)
