# 写一个爬虫re案例
import requests
import re

# 请求天气网站
response = requests.get('http://www.weather.com.cn/weather/101010100.shtml')
response.encoding = 'utf-8'

# 获取天气信息
pattern = re.compile('<h1>(.*?)</h1>.*?"wea">(.*?)</p>.*?<em>(.*?)</em>.*?<b>(.*?)</b>', re.S)
match = pattern.search(response.text)

if match:
    city = match.group(1)
    weather = match.group(2)
    temperature = match.group(3)
    wind = match.group(4)
    print(f"{city}天气：{weather}，温度：{temperature}，风力：{wind}")
else:
    print("未找到天气信息")

response.close()
