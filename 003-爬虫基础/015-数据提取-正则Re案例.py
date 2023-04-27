import requests
import re

# 发送请求获取天气信息
response = requests.get('http://www.weather.com.cn/weather/101010100.shtml')  # 发送请求
response.encoding = 'utf-8'  # 设置编码格式

# 解析天气信息
# 编译正则表达式，匹配天气信息中的城市、天气、温度和风力
pattern = re.compile('<h1>(.*?)</h1>.*?"wea">(.*?)</p>.*?<em>(.*?)</em>.*?<b>(.*?)</b>', re.S)
match = pattern.search(response.text)  # 在响应文本中搜索匹配项

# 提取天气信息并打印
if match:
    city = match.group(1)  # 获取城市信息
    weather = match.group(2)  # 获取天气信息
    temperature = match.group(3)  # 获取温度信息
    wind = match.group(4)  # 获取风力信息
    print(f"{city}天气：{weather}，温度：{temperature}，风力：{wind}")  # 打印天气信息
else:
    print("未找到天气信息")  # 如果没有匹配项，则打印未找到天气信息

response.close()  # 关闭响应

