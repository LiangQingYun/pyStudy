import requests

url = 'https://www.baidu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41'
}
# 这里是URL问号后面的内容
kw = {

}

with requests.get(url, headers=headers , params=kw) as response:
    response.encoding = 'utf-8'
    print(response.text)
