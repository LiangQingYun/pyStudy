import requests

# 方式一：在headers中添加cookie
url = 'https://www.baidu.com/'
headers = {
    'Cookie': '这里写对应的cookie值',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41'
}

with requests.post(url, headers=headers) as response:
    response.encoding = 'utf-8'
    print(response.text)

# 方式二 : 使用requests库中的cookies参数
cookies = {'name1': 'value1', 'name2': 'value2'}

response = requests.get('https://example.com', cookies=cookies)
# 方式三 : 使用session对象
import requests

# 创建 Session 对象
session = requests.Session()

# 添加 cookie (或者你请求一次，然后获取到cookie，然后再添加)
session.cookies.set('uid', '123456')

# 发送 GET 请求并自动带上 cookie
response = session.get('http://www.example.com')

# 发送 POST 请求并自动带上 cookie
response = session.post('http://www.example.com', data={'key': 'value'})
