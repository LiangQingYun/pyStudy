# -*- coding: utf-8 -*-
import requests
import time
import hashlib
n = str(int(time.time() * 1000))
def MD5Test():
    text = n + "9527" + n[:6]
    return hashlib.md5(text.encode()).hexdigest()
headers = {
    "authority": "api.mytokenapi.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-GB,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded;charset=utf-8",
    "origin": "https://www.mytokencap.com",
    "pragma": "no-cache",
    "referer": "https://www.mytokencap.com/",
    "sec-ch-ua": "^\\^Google",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\\^Windows^^",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}
url = "https://api.mytokenapi.com/ticker/index"
params = {
    "pages": "3,1",
    "sizes": "100,100",
    "subject": "market_cap",
    "last_id": "242196841.06",
    "language": "en_US",
    "timestamp": n,
    "code": MD5Test(),
    "platform": "web_pc",
    "v": "0.1.0",
    "legal_currency": "USD",
    "international": "1"
}
response = requests.get(url, headers=headers, params=params)
print(response.text)
print(response)



