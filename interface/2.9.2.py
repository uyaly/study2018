# coding:utf-8
import requests
# 请求头
headers = {
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
}
url = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
s = requests.session()
# 打开我的随笔
r = s.get(url, headers=headers, verify=False, allow_redirects = False)
# 打印状态码，自动处理重定向请求
print r.status_code
new_url = r.headers["Location"]
print new_url