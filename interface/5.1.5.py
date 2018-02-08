# coding:utf-8
from bs4 import BeautifulSoup
import requests
r = requests.get(r"http://www.cnblogs.com/yoyoketang/")
# 请求首页后获取整个html界面
blog = r.content
# 用html.parser解析html
soup = BeautifulSoup(blog, "html.parser")
# 获取所有的class属性为dayTitle，返回Tag类
# times = soup._find_all(class_="dayTitle")
times = soup.find_all(class_="postDesc")

title = soup.find_all(class_="postTitle")
descs = soup.find_all(class_="postCon")

for i,j,k in zip(times, title, descs):
    # print i.a.string
    print j.a.string
    print k.div.contents[0]
    print ""
