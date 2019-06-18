# coding:utf-8
import requests

url = "http://192.168.3.116/vmsBS/monitor/"

querystring = {"username":"system","password":"system@123","orgCode":"B"}

headers = {
    'cache-control': "no-cache",
    'Postman-Token': "89fe7903-481a-425b-92db-1eb8bad7cf65"
    }

response = requests.request("POST", url + r'login.do', headers=headers, params=querystring)

# print(response.text)

querystring = {"typeName":"2","selectStatus":"2","startDate":"2019-01-01%2010:07:00","endDate":"2019-01-31%2010:07:00","page":"1","rows":"50"}

# headers = {
#     'User-Agent': "PostmanRuntime/7.13.0",
#     'Accept': "*/*",
#     'Cache-Control': "no-cache",
#     'Postman-Token': "210bf8f6-1490-4c60-9be7-fcbca61e3028,dcf04b90-6f7f-4aac-ba6a-28be605a8c05",
#     'Host': "192.168.3.116",
#     'cookie': "JSESSIONID=HqHvYz1H3oNQDJZPVhJ2F0oLZmYJ72JKneDuvYuwjVSp0BnTcH0T!1343646499",
#     'accept-encoding': "gzip, deflate",
#     'content-length': "",
#     'Connection': "keep-alive",
#     'cache-control': "no-cache"
#     }

response = requests.request("POST", url + 'newAlarmData.do', headers=headers, params=querystring)

print(response.text)