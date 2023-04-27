import re
import requests

result_set = set()  # 定义一个集合，用于存放匹配到的小说名称

# 发送 GET 请求，获取 HTML 页面内容
for i in range(1, 10, 1):
    url = f'https://www.qqxsnew.net/list/1-{i}.html'
    response = requests.get(url)
    html_doc = response.text
    pattern = r'<span class="s2"><a href=".*?">(.*?)</a></span>'
    results = re.findall(pattern, html_doc)
    if results:
        for result in results:
            result_set.add(result)

print(result_set)


