# coding:utf-8
# 引入unittest模组
import unittest
# 引入WebDriver包
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select   # 导入select方法
# 模拟键盘的操作需要先导入键盘模块
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
# 引入WebDriver Keys包
from selenium.webdriver.common.keys import Keys
# 定义测试类，名字为logintest
# 该类必须继承unittest.TestCase基类
class logintest(unittest.TestCase):
    # 使用'@'修饰符，注明该方法是类的方法
    # setUpClass方法是在执行测试之前需要先调用的方法
    # 是开始测试前的初始化工作
    @classmethod
    def setUpClass(cls):
        # 创建浏览器对象
         cls.driver = webdriver.Firefox()
         cls.driver.get("http://47.52.77.154:8015/Default/Login")
        # 浏览器最大化
         cls.driver.maximize_window()

        # cls.title = EC.title_is(u'轰扑克皇家俱乐部')
        #  print (cls.driver.title)
         print(" -- set up finished -- ")
         print
    # 测试一（务必以test开头）
    def test_01login(self):
        self.driver.implicitly_wait(10)
        # 清除当前的输入
        self.driver.find_element_by_id("txtaccount").clear()
        self.driver.find_element_by_id('txtpassword').clear()
        # 输入用户名和密码，进行登录
        self.driver.find_element_by_id('txtaccount').send_keys("kaka")
        self.driver.find_element_by_id('txtpassword').send_keys("a123")
        self.driver.find_element_by_id('btlogin').click()
    # def test_02logout(self):
    #     self.exit = self.driver.find_element_by_id("loginOut")
    #     self.assertEqual('退出', exit.text)
    #     print(exit.get_attribute('type'))
    #     print
    #     print('-- test_01 login finished -- ')
    #     print

    # 测试二（务必以test开头）
    def test_02(self):
        self.driver.implicitly_wait(10)
        # 进入模块
        self.driver.find_element_by_xpath(".//*[@id='navi']/div/div/div[3]/div/a/em").click()
        self.driver.find_element_by_xpath(".//*[@id='navi']/div/div/div[3]/ul/li[2]/a").click()
        self.driver.implicitly_wait(10)
        # 点击新增按钮
        # js = 'document.getElementById("add_Link").click();'
        # self.driver.execute_script(js)
        iframe1 = self.driver.find_element_by_id("mainIframe")
        self.driver.switch_to.frame(iframe1)
        # 感谢QQ：326186713 流年斑驳XXXXXX,input标签中的按钮要用send_keys(Keys.ENTER)来点击
        self.driver.find_element_by_id('add_Link').send_keys(Keys.ENTER)
        self.driver.implicitly_wait(3)
        # 释放iframe，重新回到主页上XXXXXX,iframe一定要切回来
        self.driver.switch_to.default_content()
        # 新增界面
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id("_easyui_textbox_input1").send_keys('ccd0')
        # self.driver.find_element_by_css_selector("#_easyui_textbox_input10").send_keys('ccd0')
        self.driver.implicitly_wait(3)
        # 这里要滚动过
        js1 = 'document.getElementById("form").scrollTop=10000'
        self.driver.execute_script(js1)
        self.driver.find_element_by_id("_easyui_textbox_input17").send_keys('cd0')
        # self.driver.implicitly_wait(5)
        # self.driver.find_element_by_id("_easyui_textbox_input23").send_keys('a123')
        # self.driver.implicitly_wait(3)
        # self.driver.find_element_by_id('_easyui_textbox_input24').send_keys('a123')
        # self.driver.implicitly_wait(3)
        # self.driver.find_element_by_id("_easyui_textbox_input18").send_keys('ccd0')
        # self.driver.implicitly_wait(3)
        # self.driver.find_element_by_id("_easyui_textbox_input20").send_keys('15555555555')
        # self.driver.implicitly_wait(10)
        # # self.driver.find_element_by_id('loginOut').click()
        # self.driver.find_element_by_css_selector("span.l-btn-text").click()
        # self.driver.find_element_by_link_text("确定").click()
        # self.driver.implicitly_wait(10)
        print('-- test 02 finished -- ')

    # tearDownClass方法是执行完所有测试后调用的方法
    # 是测试结束后的清除工作
    @classmethod
    def tearDownClass(self):
        # 关闭浏览器
      self.driver.quit()

# 执行测试主函数
if __name__ == '__main__':
    # 执行main全局方法，将会执行上述所有以test开头的测试方法
   unittest.main(verbosity=2)