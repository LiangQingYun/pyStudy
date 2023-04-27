import requests


"""
    透明代理 不建议使用
    匿名代理 别人只能知道你用了代理，但是不知道你的真实IP
    高匿代理 别人不知道你用了代理，也不知道你的真实IP (付费用这个)
"""
url = 'https://www.baidu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41'
}

proxies = {
    'http': 'http://:',  # 代理IP:端口号
}

with requests.post(url, headers=headers, proxies=proxies) as response:
    response.encoding = 'utf-8'
    print(response.text)
