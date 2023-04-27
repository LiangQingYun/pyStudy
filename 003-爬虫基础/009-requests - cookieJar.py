import requests

"""
我们首先发送了一个GET请求，并从响应中获取了cookiejar。
然后，我们使用requests.utils.dictfromcookiejar函数将cookiejar转换为字典，并将结果存储在cookiesdict变量中。

在cookie逆向的时候会用到
"""

url = "http://www.baidu.com"
response = requests.get(url)

cookies = response.cookies
cookies_dict = requests.utils.dict_from_cookiejar(cookies)

print(cookies_dict)
