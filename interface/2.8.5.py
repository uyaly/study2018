# coding:utf-8
import requests
url = "http://www.kuaidi.com/index-ajaxselectcourierinfo-1202247993797-yunda.html"
headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0" }
# get方法加个ser-Agent就可以了
s = requests.session()
r = s.get(url, headers=headers, verify=False)
result = r.json()
data = result["data"]
# 获取data里面内容
print data
print data[0]
#  获取data里最上面有个
get_result = data[0]['context']
# 获取已签收状态
print get_result
print data[0]['time']
if u"已签收" in get_result:
    print "快递单已签收成功"
else:
    print "未签收"