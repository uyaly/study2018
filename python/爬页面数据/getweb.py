
#-*-coding:utf-8-*-
 
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

key = u"全"
def get_content(url, headers, key):
    '''
    @获取403禁止访问的网页
    '''
    randdom_header=random.choice(headers)

    req=urllib2.Request(url)
    req.add_header("User-Agent",randdom_header)
    # req.add_header("Host","blog.csdn.net")
    # req.add_header("Referer","http://blog.csdn.net/")
    req.add_header("GET",url)
    result = []
    result_text = []
    content=urllib2.urlopen(req).read()
    # 所有id包含normalthread_的
    result_text_temp = etree.HTML(content).xpath('//*[contains(@id, "normalthread_")]/tr/th/a[1]/text()')
    result_link = etree.HTML(content).xpath('//*[contains(@id, "normalthread_")]/tr/th/a[1]/@href')
    # print len(result_text)
    # print len(result_link)

    for i in range(len(result_text_temp)):
        # print i
        result_text.append(result_text_temp[i])
        if key in result_text[i]:
            # result_ = result_text[i] + result_link[i]
            result.append(result_text[i] + '  ' + result_link[i])
            print result_text[i]
            print result_link[i]
    return result


print get_content(url,my_headers,key)
