# -*- coding: utf-8 -*-

import requests

params = {
    'pwd':'12345123123123123123123678'
}
res = requests.get('http://127.0.0.1:8080/api',params=params)

data = {
    'name':'娜娜'
}
print(requests.post('http://127.0.0.1:8080', data=data).text)
# print(res.text)

