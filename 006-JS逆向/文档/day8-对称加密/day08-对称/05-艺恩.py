import json

import requests
import execjs
from pprint import pprint

cell = execjs.compile(open('04-des.js',encoding='utf-8').read())


def get_index(url):
    headers = {
        "Host": "www.endata.com.cn",
        "Pragma": "no-cache",
        "sec-ch-ua": "\"Google Chrome\";v=\"111\", \"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"111\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    }
    data = {
        'startTime': '2023-05-01',
        'MethodName': 'BoxOffice_GetMonthBox'
    }
    res = requests.post(url=url, headers=headers,data=data)
    response = cell.call('des_decrypt',res.text)
    pprint(json.loads(response))



if __name__ == '__main__':
    get_index('https://www.endata.com.cn/API/GetData.ashx')
