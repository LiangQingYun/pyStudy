# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class ScrapySpiderSpiderMiddleware:
    # 并非所有方法都需要定义。如果方法未定义，Scrapy 将会认为爬虫中间件不会修改传入的对象。
    @classmethod
    def from_crawler(cls, crawler):
        # 这个方法被 Scrapy 用于创建您的爬虫。
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # 当每个响应通过爬虫中间件进入爬虫时被调用。
        # 应该返回 None 或引发异常。
        return None

    def process_spider_output(self, response, result, spider):
        # 在 Spider 处理响应后，通过 Spider 返回结果时被调用。
        # 必须返回可迭代的 Request 或 item 对象。
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # 当爬虫或 process_spider_input() 方法（来自其他爬虫中间件）引发异常时被调用。
        # 应该返回 None 或可迭代的 Request 或 item 对象。
        pass

    def process_start_requests(self, start_requests, spider):
        # 与 process_spider_output() 方法类似，但没有关联响应的起始请求。
        # 必须只返回请求（不包含 item）。
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ScrapySpiderDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    # 类似初始化
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    #  每个请求在通过downloader下载中间件时都会调用该方法。类似于拦截请求重新处理
    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request (继续请求)
        # - or return a Response object (返回一个响应对象,交给引擎返回给Spider)
        # - or return a Request object  (返回一个请求对象,交给调度器重新处理)
        # - or raise IgnoreRequest: process_exception() methods of (抛出异常)
        #   installed downloader middleware will be called (下载中间件的process_exception()方法将被调用)
        return None

    # 下载器下载完之后, 会调用该方法, 传入的参数是下载器下载完之后的响应对象
    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object (返回一个响应对象,交给引擎返回给Spider)
        # - return a Request object (返回一个请求对象,交给调度器重新处理)
        # - or raise IgnoreRequest (抛出异常)
        return response

    # 当下载器下载过程中出现异常时, 会调用该方法, 传入的参数是异常对象
    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception (继续处理异常)
        # - return a Response object: stops process_exception() chain (返回一个响应对象,交给引擎返回给Spider)
        # - return a Request object: stops process_exception() chain (返回一个请求对象,交给调度器重新处理)
        pass

    # 当爬虫中间件开始执行时, 会调用该方法
    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

# 需要在配置文件开启 DOWNLOADER_MIDDLEWARES (类名非固定,自定义的)
class proxyDownloaderMiddleware(object):
    # 代理IP
    proxy_list = [
        'http://'
    ]
