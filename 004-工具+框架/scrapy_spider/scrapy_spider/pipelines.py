# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapySpiderPipeline:

    # 开始爬虫时会执行一次
    def open_spider(self, spider):
        print("爬虫开始了")

    # 结束爬虫时会执行一次
    def close_spider(self, spider):
        print("爬虫结束了")

    # 每一个item都会执行一次
    def process_item(self, item, spider):
        print(item)
        # 这里如果不返回item，那么数据就不会传递到下一个管道 会报 TypeError: 'NoneType' object is not iterable
        return item


