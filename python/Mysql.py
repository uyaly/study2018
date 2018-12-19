
# coding:utf-8
import MySQLdb as mdb
import sys

#连接mysql，获取连接对象
con = mdb.connect('localhost', 'root', 'test');

with con:
    #仍然是，第一步获取连接的cursor对象，用于执行查询
    cur = con