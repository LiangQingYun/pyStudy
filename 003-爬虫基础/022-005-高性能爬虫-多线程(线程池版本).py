import threading
import time
from concurrent.futures import ThreadPoolExecutor

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
            # "session": "798d989db7b0d25c173abb384d4911fb",
            "three_category_id": "15"
        }
        self.headers = {
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
        }
        self.lock = threading.Lock()

    def get_data(self):
        for page_id in range(1, 10):
            self.data['page_id'] = page_id
            # 获取数据
            response = requests.get(url=self.url, headers=self.headers, params=self.data)
            response.encoding = 'utf-8'
            self.parse_data(response.json())

    def parse_data(self, data):
        # 解析数据
        videos = data['data']['list']
        for video in videos:
            item = {'title': video['title'], 'playUrl': video['playUrl'], 'description': video['description']}
            self.save_data(item)

    def save_data(self, data):
        global count
        # 这里加了锁 , 所以相当于单线程了
        with self.lock:
            with open('data.txt', 'a', encoding='utf-8') as f:
                f.write(f"{count}: {data}\n")
                count += 1

    def main(self):
        # 主函数
        self.get_data()
        with ThreadPoolExecutor(max_workers=5) as pool:
            for item in range(1, 10):
                pool.submit(self.get_data, item)


if __name__ == '__main__':
    start_time = time.time()
    i = IQiYi()
    i.main()
    print("总耗时: ", round(start_time - time.time(), 2), "秒" + "总共爬取了", count, "条数据")
