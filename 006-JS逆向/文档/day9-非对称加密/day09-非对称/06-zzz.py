# -*- coding: utf-8 -*-


import requests
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")
# 修改编码方式,window默认编码是gbk,Mac和Linux 默认是uft-8

import execjs

headers = {
        "authority": "api.wei-liu.com",
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "en-GB,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "origin": "https://www.wei-liu.com",
        "pragma": "no-cache",
        "referer": "https://www.wei-liu.com/",
        "sec-ch-ua": "^\\^Google",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "^\\^Windows^^",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
    }
def get_code():
    url = "https://api.wei-liu.com/api/v1/Token/code"
    res= requests.get(url,headers=headers)
    data = res.json().get('data')
    return data.get('item1'),data.get('item2')

def get_login():
    item1,itme2 = get_code()
    cell = execjs.compile(open('05-留云.js',encoding='utf-8').read())
    pwd = cell.call('get_pwd',item1,itme2,'12345678')
    url = "https://api.wei-liu.com/api/v1/Token"
    data = {"username":"admin","password":pwd,"code":"","grant_type":"password","userType":1,"language":"zh-CN"}
    response = requests.post(url, headers=headers, json=data)
    print(response.text)
    print(response)
get_login()


