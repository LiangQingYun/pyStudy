


import requests


url = ''
# 设置超时时间为5秒   一般和代理一起使用 ,避免代理失效等待时间过长
response = requests.get(url, timeout=5)
