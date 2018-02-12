import requests

url = "http://192.168.3.65:14011/oauth/token"

payload = {"password":"000000", "username":"13800000007", "grant_type":"password", "scope":"app", "client_secret":"secret", "client_id":"client"}
headers = {
    'content-type': "application/json;charset=UTF-8",
    'Cache-Control': "no-cache",
    # 'Postman-Token': "77f158b5-c85c-5e5a-1fd9-7340521010a1"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)