# coding:utf-8
from selenium import webdriver
from lxml import etree
#from selenium.webdriver.chrome.options import Options
import time
import datetime

#chrom_options = Options()
#chrom_options.add_argument('--headless')
#chrom_options.add_argument('--disable-gpu')

#driver = webdriver.Chrome(chrome_options=chrom_options)
#指定浏览器为Chrome浏览器
driver = webdriver.Chrome('D:\Program Files (x86)\Appium\node_modules\appium\node_modules\appium-chromedriver\chromedriver\win\chromedriver.exe')
#窗体最大化
# driver.maximize_window()

def login(url):
    '''
    这是登录模块,用于登录淘宝，并选中需要购买的商品的
    :param url:  https://login.taobao.com/构件/ login.jhtml
    :return: 无
    '''
    #获取网页源信息
    driver.get(url)
    #等浏览器与Selenium完美契合之后再进行下一步动作
    driver.implicitly_wait(10)
    #等待10秒
    time.sleep(10)
    #查找购物车按钮的xpath并点击进入购物车
    driver.find_element_by_xpath('//*[@id="mc-menu-hd"]/span[2]').click()
    #等待4秒
    time.sleep(4)
    #勾选你需要购买的物品，这里勾选的是华为mate20.反正我也没钱买，不如直接给你们做个示范
    driver.find_element_by_xpath('//*[@id="J_Item_951817163433"]/ul/li[1]/div/div/label').click()
    #等待5秒
    time.sleep(5)

def buy_good(buy_time):
    '''
    登录页面之后，这个程序就一直循环读取当前的系统时间，如果到了开始秒抢的时间，立马启动程序开始提交订单
    :param buy_time: 给定的秒抢时间
    :return: 无
    '''
    #一直循环读取系统时间，等待秒强开始
    while True:
        #读取系统当前时间
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #是否到可以购买的时间了
        if now_time == buy_time:
            try:
                #“//*[@id="J_Go"]/span”是我添加的商品你的xpath，你需要更换为你需要的商品的xpath，否则爬虫会失败
                #这一句是判断，是否可以购买了
                if driver.find_element_by_xpath('//*[@id="J_Go"]/span'):
                    # 点击立即购买按钮
                    driver.find_element_by_xpath('//*[@id="J_Go"]/span').click()
                    # 点击提交订单按钮
                    driver.find_element_by_xpath('//*[@id="submitOrder_1"]/div/a[2]').click()
                    # 然后你就可以输入密码进行支付了
                    #结束循环
                    break
            except:
                time.sleep(1)
        print(now_time)
        time.sleep(1)

if __name__ == "__main__":
    url = 'https://login.taobao.com/member/login.jhtml'
    login(url=url)
    buy_good('2018-11-29 14:23:13')
