# 写一个url打开网页爬取数据
import urllib.request

# 打开一个url，返回一个对象
response = urllib.request.urlopen('http://www.baidu.com')
# 读取对象的内容
html = response.read()
# 打印内容
print(html)

# 保存html到文件
with open('baidu.html', 'wb') as f:
    f.write(html)

response.close()  # 关闭对象
