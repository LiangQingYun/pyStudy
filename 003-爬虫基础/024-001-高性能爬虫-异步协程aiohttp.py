"""
    多个操作无关联性的时候，可以使用异步协程
    异步协程使得程序可以在执行I/O等阻塞操作时不会被阻塞 --对应单个线程的操作

    requests就是同步操作，当请求一个网页的时候，程序会一直等待，直到请求到网页为止
    用异步协程，当请求一个网页的时候，程序会继续执行，不会等待，直到请求到网页为止

    爬虫中用到这个就是优化网络请求，提高效率
"""
import aiohttp
import asyncio

async def download_image(session, url, file_path):
    response = await session.get(url)
    with open(file_path, 'wb') as f:
        f.write(await response.read())  # 取值的时候也要加await   read是二进制数据


async def main():
    urls = ['https://wzzsmanager-1255653016.file.myqcloud.com/common-image/b61762c404cc68a90a8993b443a0b0ec.jpeg',
            'https://wzzsmanager-1255653016.file.myqcloud.com/common-image/fb4f4e066bed51078ea39cd210b5a6c9.jpeg',
            'https://wzzsmanager-1255653016.file.myqcloud.com/common-image/c3abbd201774097b5231117bc8caa7bf.jpeg']

    async with aiohttp.ClientSession() as session:
        tasks = []
        for i, url in enumerate(urls):
            file_path = f'../10010-image/{i}.jpeg'
            tasks.append(asyncio.create_task(download_image(session, url, file_path)))
        # await asyncio.gather(*tasks)
        await asyncio.wait(tasks)

if __name__ == '__main__':
    """
        asyncio.run(main()) 会自动创建一个事件循环，然后在这个事件循环中执行main()协程, 会自动关闭循环
        而loop.run_until_complete(main())不会
    """
    # asyncio.run(main())

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

    print('下载完成')
