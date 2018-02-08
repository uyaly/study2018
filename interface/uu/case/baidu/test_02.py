# coding:utf-8
import unittest

class Test1(unittest.TestCase):
    def setUp(self):
        print("start!")

    def tearDown(self):
        print("end!")

    def test_01(self):
        a = 1
        b = 2
        self.assertTrue(3, a+b)

    def test_02(self):
        a = 3
        b = 2
        self.assertTrue(6, a*b)

    def test_03(self):
        import requests

        url = "http://59.172.105.83:81/vmsBS/monitor/login.do"

        # payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"username\"\r\n\r\nsystem\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\nsystem@123\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"orgCode\"\r\n\r\nB\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        payload = {"username":"system","password":"system@123","orgCode":"B"}
        # headers = {
            # 'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            # 'Cache-Control': "no-cache",
            # 'Postman-Token': "653764e1-3b08-bfb1-9747-1db251b405ff"
            # }
        headers = {
                    "content-type": "application/x-www-form-urlencoded",
                    "Cache-Control": "no-cache",
                    "Postman-Token": "653764e1-3b08-bfb1-9747-1db251b405ff"
                    }
        response = requests.request("POST", url, data=payload, headers=headers)

        print(response.text)

if __name__ == "__main__":
    unittest.main()