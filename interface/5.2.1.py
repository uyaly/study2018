# coding:utf-8
from bs4 import BeautifulSoup
yoyo = open("5.2.1.html")

# 5.2.1
# print yoyo.read()

# 5.2.2
soup = BeautifulSoup(yoyo)
# prettify(）可以自动解析成html格式
print soup.prettify()
