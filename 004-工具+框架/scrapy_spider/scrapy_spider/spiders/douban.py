import sys

import scrapy
from scrapy import cmdline


class DoubanSpider(scrapy.Spider):
    # 爬虫名字
    name = 'douban'
    # 允许爬取的域名
    allowed_domains = ['movie.douban.com']
    # # 起始的url
    # start_urls = ['https://movie.douban.com/top250?start=25&filter=']

    def start_requests(self):
        # 重写start_requests方法，将start_urls中的url交给调度器
        for i in range(0, 1):
            url = 'https://movie.douban.com/top250?start={}&filter='.format(i * 25)
            yield scrapy.Request(url=url, callback=self.parse)

    # 解析数据
    def parse(self, response, **kwargs):
        print("目前使用的解释器:  " + sys.executable)
        # print(response.encoding)  # 编码
        # scrapy的response对象可以直接进行xpath
        ol_list = response.xpath('//ol[@class="grid_view"]/li')
        for ol in ol_list:
            # 创建一个数据字典
            item = {}
            # 利用scrapy封装好的xpath选择器定位元素，并通过extract()或extract_first()来获取结果
            item['title'] = ol.xpath('.//div[@class="hd"]/a/span[1]/text()').extract_first()
            item['rating'] = ol.xpath('.//div[@class="bd"]/div/span[2]/text()').extract_first()
            item['quote'] = ol.xpath('.//div[@class="bd"]//p[@class="quote"]/span/text()').extract_first()
            # print(item)
            # 将数据交给引擎 引擎就数据交给管道 (需要在settings.py中开启管道)
            # yield能够传递的对象只能是：BaseItem,Request,dict,None**
            # yield item
            details_url = ol.xpath('.//div[@class="hd"]/a/@href').extract_first()
            print(details_url)
            # 是要将这个请求 ,返回给引擎, 引擎再交给调度器走下载中间件
            yield scrapy.Request(url=details_url, meta={'item': item}, callback=self.parse_detail)
    def parse_detail(self, response):
        item = response.meta['item']
        item['release_date'] = response.xpath('//span[@property="v:initialReleaseDate"][1]/text()').extract_first()
        yield item


if __name__ == '__main__':
    cmdline.execute("scrapy crawl douban".split())
    # cmdline.execute("scrapy crawl douban --nolog".split()) # 不显示日志
    # cmdline.execute("scrapy crawl douban -o douban.csv".split()) # 保存为csv文件
    # cmdline.execute("scrapy crawl douban -o douban.json".split()) # 保存为json文件
    # cmdline.execute("scrapy crawl douban -o douban.xml".split()) # 保存为xml文件
    # cmdline.execute("scrapy crawl douban -o douban.jsonlines".split()) # 保存为jsonlines文件
    # cmdline.execute("scrapy crawl douban -o douban.yml".split()) # 保存为yml文件
