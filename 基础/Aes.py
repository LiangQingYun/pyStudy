import binascii
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
import requests

url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="

i0x = {
    "rid": "A_PL_0_919620061",
    "threadId": "A_PL_0_919620061",
    "pageNo": "1",
    "pageSize": "20",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "csrf_token": ""
}

def b(a, b):
    key = b.encode('utf-8')
    iv = b'0102030405060708'
    data = a.encode('utf-8')
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_data = cipher.encrypt(pad(data, AES.block_size))
    return base64.b64encode(encrypted_data).decode('utf-8')


# 这就是那个巨坑的 c 函数
def c(text,b, c):
    e = b
    f = c
    text = text[::-1]
    result = pow(int(binascii.hexlify(text.encode()), 16), int(e, 16), int(f, 16))
    return format(result, 'x').zfill(131)

def asrsea(d):
    e = "010001"
    f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
    g = "0CoJUm6Qyw8W8jud"
    i = "ARo2AVwAyEDk7vj4"
    encText = b(d, g),
    encText = b(encText[0], i),
    encSecKey = c(i, e, f),
    print(encText)
    print(encSecKey)
    return encText, encSecKey



if __name__ == '__main__':
    ddd = asrsea(json.dumps(i0x))

    response = requests.post(url, {
        "params": ddd[0],
        "encSecKey": ddd[1]
    })
    # 获取响应数据
    response.encoding = 'utf-8'
    page_text = response.text
    page_text = json.loads(page_text)
    print(page_text)
