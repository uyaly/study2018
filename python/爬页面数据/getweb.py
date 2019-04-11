#-*-coding:utf-8-*-
import time
import urllib2
import random
from lxml import etree
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
url="http://www.deyi.com/forum-23-1.html"
 
my_headers=["Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"
]

def get_content(url, key):
    '''
    @获取403禁止访问的网页
    '''
    randdom_header=random.choice(my_headers)

    req=urllib2.Request(url)
    req.add_header("User-Agent",randdom_header)
    req.add_header("GET",url)
    result_text = []
    result_link = []
    content=urllib2.urlopen(req).read()
    # 所有id包含normalthread_的
    result_text_temp = etree.HTML(content).xpath('//*[contains(@id, "normalthread_")]/tr/th/a[1]/text()')
    result_link_temp = etree.HTML(content).xpath('//*[contains(@id, "normalthread_")]/tr/th/a[1]/@href')
    for i in range(len(result_text_temp)):
        if key in result_text_temp[i]:
            result_text.append(result_text_temp[i])
            result_link.append(result_link_temp[i])
    return result_text,result_link

def refresh(str, interval):
    if str == " 开 始 ":
        for j in range(int(interval)):
            str = ' ' + str(int(interval)-j) + ' '
            time.sleep(1)
        refresh()
        # out_text.after(int(interval)*1000, refresh) #  单位是毫秒，1秒(s)=1000毫秒(ms)
    else:
        # b['state'] = "normal"
        str = " 开 始 "