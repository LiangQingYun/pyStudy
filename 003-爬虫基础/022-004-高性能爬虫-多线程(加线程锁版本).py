import queue
import threading
import time

import requests

count = 0


class IQiYi:
    def __init__(self):
        self.url = "https://pcw-api.iqiyi.com/search/recommend/list"
        self.data = {
            "channel_id": 2,
            "data_type": 1,
            "mode": 11,
            "page_id": 1,
            "ret_num": 48,
            "three_category_id": "15"
        }
        self.headers = {
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
        }
        self.url_queue = queue.Queue()
        self.data_queue = queue.Queue()
        self.parse_queue = queue.Queue()

        self.lock = threading.Lock()  # 新增线程锁

    # 生成分页的URL参数
    def get_url(self):
        for page_id in range(1, 10):
            self.data['page_id'] = page_id
            # 获取URL
            self.url_queue.put(self.data)

    # 通过URL获取数据
    def get_data(self):
        while True:
            # 在队列中获取URL参数
            params = self.url_queue.get()
            response = requests.get(url=self.url, headers=self.headers, params=params, timeout=3)
            response.encoding = 'utf-8'
            self.data_queue.put(response.json())  # 将数据放入解析队列
            self.url_queue.task_done()  # 在处理完数据之后, 通知队列, 这个数据已经被取出来了(手动减一)

    def parse_data(self):
        while True:
            # 解析数据
            data = self.data_queue.get()
            videos = data['data']['list']
            for video in videos:
                item = {'title': video['title'], 'playUrl': video['playUrl'], 'description': video['description']}
                self.parse_queue.put(item)
            self.data_queue.task_done()  # 在处理完数据之后, 通知队列, 这个数据已经被取出来了(手动减一)

    def save_data(self):

        while True:
            with self.lock:  # 获取线程锁
                # 保存数据
                item = self.parse_queue.get()
                global count
                with open('data.txt', 'a', encoding='utf-8') as f:
                    f.write(f"{count}: {item}\n")
                    count += 1
                self.parse_queue.task_done()  # 在处理完数据之后, 通知队列, 这个数据已经被取出来了(手动减一)

    # 主函数
    def main(self):
        self.get_url()
        threads = []
        for threadIter in range(9):
            # 请求数据可以多线程 设置九个线程
            threads.append(threading.Thread(target=self.get_data))
        for threadIter in range(3):
            # 解析数据可以多线程  设置两个线程
            threads.append(threading.Thread(target=self.parse_data))
            # 保存数据可以多线程,但是写文件要注意锁的问题 (可以用一个线程写数据)
            threads.append(threading.Thread(target=self.save_data))
        for t in threads:
            t.daemon = True  # 把子线程设置为守护线程，主线程结束，子线程也结束
            t.start()
        for q in [self.url_queue, self.data_queue, self.parse_queue]:
            # 这是一个阻塞方法，当队列中的数据全部被取出后，才会执行后面的代码,主线程才会退出
            q.join()


if __name__ == '__main__':
    start_time = time.time()
    i = IQiYi()
    i.main()
    print("总耗时: ", round(time.time() - start_time, 2), "秒" + "总共爬取了", count, "条数据")  # 数据总条数应该是432条
