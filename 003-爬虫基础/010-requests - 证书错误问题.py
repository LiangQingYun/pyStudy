"""
当你使用Python进行爬虫时，有时会出现SSL证书不受信任或不安全的问题。这是因为SSL证书用于保护网站数据传输的安全，
而有些网站的证书不是由受信任的机构颁发的，或者证书已经过期，因此Python默认不信任这些证书。

"""

# 方式一 : 忽略证书验证。这种方法不太安全，因为你可能会向一个不受信任的网站发送敏感信息。但如果你只是想浏览一些不重要的网站，这种方法也是可行的。
import requests

response = requests.get('https://example.com', verify=False)

# 方式二 : 使用证书验证。这种方法比较安全，因为你可以使用受信任的证书来验证网站。
# 首先，你需要从该网站下载证书文件。然后，你可以使用 cert 参数来将证书添加到请求中
import requests

response = requests.get('https://example.com', cert='/path/to/certfile')
