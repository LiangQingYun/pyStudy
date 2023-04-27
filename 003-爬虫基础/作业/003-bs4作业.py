import requests
from bs4 import BeautifulSoup

url = "http://ip.yqie.com/ipproxy.htm"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'lxml')

# 获取所有IP信息的表格
table = soup.find('table')

# 获取所有IP信息行
rows = table.find_all('tr')


# 遍历每行IP信息
for row in rows[1:]:
    # 获取代理IP地址
    ip = row.find_all('td')[0].text.strip()
    # 获取端口
    port = row.find_all('td')[1].text.strip()
    # 获取服务器地址
    server = row.find_all('td')[2].text.strip()
    # 获取是否匿名
    is_anonymous = row.find_all('td')[3].text.strip()
    # 获取类型
    type_ = row.find_all('td')[4].text.strip()
    # 获取存活时间
    alive_time = row.find_all('td')[5].text.strip()

    print("代理IP地址：", ip)
    print("端口：", port)
    print("服务器地址：", server)
    print("是否匿名：", is_anonymous)
    print("类型：", type_)
    print("存活时间：", alive_time)
    print("\n")