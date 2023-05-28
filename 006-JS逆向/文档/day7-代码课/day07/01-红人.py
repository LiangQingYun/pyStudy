# -*- coding: utf-8 -*-

import os

import urllib3,requests,time,json
urllib3.disable_warnings()
import hashlib
import pandas as pd
import time

iaa  = 1
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Length": "513",
    "Content-Type": "application/json;charset=UTF-8",
    "Host": "ucp.hrdjyun.com:60359",
    "Origin": "http://www.hh1024.com",
    "Pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"94\", \"Google Chrome\";v=\"94\", \";Not A Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}
times = str(int(time.time()) * 1000)

def sign(content):
    m = hashlib.md5()
    m.update(content.encode("utf8"))
    return m.hexdigest()

session = requests.session()

session.headers = headers
def login():
    times = str(int(time.time()) * 1000)
    url = 'https://user.hrdjyun.com/wechat/phonePwdLogin'
    pwd = sign('')
    sig = sign('' + pwd + times + '1' + 'JzyqgcoojMiQNuQoTlbR5EBT8TsqzJ')
    data = {
        'phoneNum': "",
        'pwd': pwd,
        'sig': sig,
        't': times,
        'tenant': 1
    }
    res = session.post(url, data=json.dumps(data))
    print(res.text)
    if res.json().get('status') == 0:
        token = res.json().get('data')['token']
        with open('token.txt', 'w') as f:
            f.write(token)
    else:
        login()

params = {"no": "dy0002", "data": {"days": 1, "rankType": 5, "liveDay": f"2023-05-21"}}
dd = json.dumps(params)
def get_sign():
    data = f'param={dd}&timestamp={times}&tenant=1&salt=kbn%&)@<?FGkfs8sdf4Vg1*+;`kf5ndl$'  # 要进行加密的数据
    data_sha = hashlib.sha256(data.encode('utf-8')).hexdigest()
    return data_sha

def get_data():
    global  iaa
    if os.path.exists('token.txt') is False:
        login()
    s = get_sign()
    t = open('token.txt', 'r').read()
    datas = {"param":dd,"sign":s,"tenant":"1","timestamp":times,"token":t}
    print(datas)
    # 数据接口
    url = 'https://ucp.hrdjyun.com:60359/api/dy'
    res = session.post(url,headers=headers,data=json.dumps(datas))
    if res.json().get('status') == 0:
        data = res.json().get('data')['rankList']
        for d in data:
            items = {}
            items['抖音名'] = d.get('anchorName')
            items['带货销量'] ='%.2f' % (d.get('salesVolume') / 10000) + '万'
            items['带货销售额'] = '%.2f' % (d.get('salesMoney') / 1000000) + '万'
            items['粉丝'] = '%.2f' % (d.get('fans') / 10000) + '万'
            items['在线人数'] = '%.2f' % (d.get('online') / 10000) + '万'
            items['时间']  =d.get('liveDay')
            print(items)

    else:
        while iaa <= 2:
            print('执行登录操作')
            login()
            time.sleep(1.5)
            iaa+=1
            get_data()

if __name__ == '__main__':
    reads = """
        本接口只开放抖音带货销量日榜
        可以根据日期查询
                                --- 夏洛
        """
    print(reads)
    get_data()
    # print(login())
