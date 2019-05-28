# coding: utf-8
import sys
# 获得系统的默认编码
# print sys.getdefaultencoding()

#  /x 转中文
s = u'\xe9\x9d\x92\xe8\x9b\x99\xe7\x8e\x8b\xe5\xad\x90'
ss = s.encode('raw_unicode_escape')
print(ss)  # 结果：b'\xe9\x9d\x92\xe8\x9b\x99\xe7\x8e\x8b\xe5\xad\x90'
# b = repr(ss)
# print unicode(eval(b),"gbk").encode('utf8')



# ss = u"\xe7\x94\xb5\xe7\xa5\xa8\xe5\x89\x8d\xe7\xbd\xae\xe4\xb8\xbb\xe6\x9c\xba"
# print(ss.encode('unicode_escape').decode('string_escape'))

# a = 'i am request,\xE6\x88\x91\xE6\x98\xAF\xE8\xAF\xB7\xE6\xB1\x82'.decode('utf-8').encode('utf-8')
# print a

ustr = u'\xca\xd3\xc6\xb5\xd7\xa5\xc8\xa1'
result = ustr.encode('raw_unicode_escape')
# result = ustr.encode('unicode_escape').decode('string_escape')
uresult = unicode(eval(repr(result)), "gbk").encode('utf8')
print (uresult)


# /u转中文

# python3的解决办法：字符串.encode('utf-8').decode('unicode_escape')
#
# python2：字符串.decode('unicode_escape')

aaa=u'\u82f1\u8bed\u8001\u5e08'
ddd=aaa.encode("gb18030").decode("gb18030")
print ddd

aaa='\u82f1\u8bed\u8001\u5e08'
b = aaa.decode('unicode_escape')
print(b)