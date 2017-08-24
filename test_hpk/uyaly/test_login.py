# coding:utf-8
import time
import unittest

import ddt
from selenium import webdriver

from test_hpk.src.test.case import ExcelUtil

# 引入WebDriver Keys包
# 测试数据
filePath = "D:\\PycharmProjects\\3\\study\\test_hpk\\data\\testdata.xlsx"
sheetName = "Sheet1"
data = ExcelUtil(filePath, sheetName)
testData = data.dict_data()
print testData
@ddt.ddt
class login(unittest.TestCase):
    u'''登录'''
    def setUp(self):
        self.driver = webdriver.Firefox()
        url = "http://47.52.77.154:8015/Default/Login"
        self.driver.get(url)
        self.driver.implicitly_wait(30)
    def login(self, username, psw):
        u'''这里写了一个登录的方法,账号和密码参数化'''
        self.driver.find_element_by_id("txtaccount").send_keys(username)
        self.driver.find_element_by_id("txtpassword").send_keys(psw)
        self.driver.find_element_by_id("btlogin").click()
        time.sleep(3)
    def is_login_sucess(self):
        u'''判断是否获取到登录账户名称'''
        try:
            return self.driver.find_element_by_id("loginTooltip").text
        except:
            return False
    @ddt.data(*testData)
    def test_login(self, data):
        u'''登录案例参考'''
        print ("当前测试数据%s"%data)
        # 调用登录方法
        self.login(data["username"], data["password"])
        # 判断结果
        result = self.is_login_sucess()
        self.assertTrue(result)
    def tearDown(self):
        self.driver.quit()
if __name__ == "__main__":
    unittest.main()