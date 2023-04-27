import requests

# 发起一个请求
search = input('请输入搜索内容：')
print(search)

url = f'https://www.sogou.com/web?query={search}'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41'
}

with requests.get(url, headers=headers) as response:
    # 获取响应数据
    response.encoding = 'utf-8'
    # 获取响应的文本数据  字符串格式(会指定编码)
    print(response.text)
    # 获取响应的文本数据   字节bytes格式(无编码)
    print(response.content)
    # 获取响应的文本数据
    print(response.json)
    # 获取响应码
    print(response.status_code)
    # 获取响应头
    print(response.headers)
    # cookies
    print(response.cookies)
    # 请求头
    print(response.request.headers)
    # 请求url
    print(response.url)


