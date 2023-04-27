"""
网站：链家网       网址：https://sh.lianjia.com/ershoufang/pudong/pg2/

用xpath做一个简单的爬虫，爬取链家网里的租房信息获取标题，位置，房屋的格局（三室一厅），关注人数，单价，总价
"""

import requests
from lxml import etree

url = "https://sh.lianjia.com/ershoufang/pudong/pg2/"

response = requests.get(url)
html = etree.HTML(response.content)

# 获取所有房源的列表
house_list = html.xpath('//ul[@class="sellListContent"]/li')

for house in house_list:
    # 获取标题
    title = house.xpath('.//div[@class="title"]/a/text()')[0]
    # 获取位置
    location = house.xpath('.//div[@class="positionInfo"]/a/text()')[0]
    # 获取格局
    layout = house.xpath('.//div[@class="houseInfo"]/text()')[0]
    # 获取关注人数
    follow = house.xpath('.//div[@class="followInfo"]/text()')[0]
    # 获取单价
    unit_price = house.xpath('.//div[@class="priceInfo"]/div[@class="unitPrice"]/span/text()')[0]
    # 获取总价
    total_price = house.xpath('.//div[@class="priceInfo"]/div[@class="totalPrice totalPrice2"]/span/text()')[0]

    print("标题：", title)
    print("位置：", location)
    print("格局：", layout)
    print("关注人数：", follow)
    print("单价：", unit_price)
    print("总价：", total_price)
    print("\n")