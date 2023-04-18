"""
    协程意义 : 用于实现并发编程
            在一个线程中如果遇到IO等待,那么线程就会阻塞,这时候就可以切换到另一个线程中执行
"""

"""
    协程的实现通常包括以下几个部分：
    
    协程函数定义：使用 async def 关键字定义一个协程函数。
    事件循环（Event Loop）：用于调度协程任务的执行顺序，类似于操作系统中的任务调度器。
    协程对象（Coroutines）：使用协程函数创建协程对象，协程对象是协程任务的表示。
    任务调度：使用事件循环调度协程对象的执行顺序，包括启动协程、暂停协程和恢复协程等操作。
    异步 IO 库支持：协程通常需要依赖异步 IO 库，如 asyncio 和 aiohttp 等，来实现协程间的通信和 IO 操作。
"""

import asyncio
import aiohttp


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def download_pages(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(asyncio.ensure_future(fetch(session, url)))
        results = await asyncio.gather(*tasks)
        return results


if __name__ == '__main__':
    urls = [
        'http://www.example.com/page1.html',
        'http://www.example.com/page2.html',
        'http://www.example.com/page3.html',
        'http://www.example.com/page4.html',
        'http://www.example.com/page5.html'
    ]

    # loop = asyncio.get_event_loop()  # 这里创建了一个事件循环
    # results = loop.run_until_complete(download_pages(urls))

    # 用run()方法来启动协程  不用自定义事件循环
    results = asyncio.run(download_pages(urls))
    print(results)
