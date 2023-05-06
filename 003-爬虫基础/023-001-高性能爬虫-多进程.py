"""
    还是多线程实用
"""
import multiprocessing
import time
from multiprocessing import JoinableQueue as Queue  # 进程有自己的专用队列
import requests

count = 0

class TencentVideo:
    def __init__(self):
        self.url = "https://pbaccess.video.qq.com/trpc.vector_layout.page_view.PageService/getPage?"
        self.headers = {'authority': 'pbaccess.video.qq.com',
                        'accept': 'application/json, text/plain, */*',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'zh-CN,zh;q=0.9',
                        'content-length': '470',
                        'content-type': 'application/json',
                        'pgv_pvid': '132225984',
                        'origin': 'https://v.qq.com',
                        'referer': 'https://v.qq.com/',
                        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-site',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
                        }

        self.url_queue = Queue()
        self.data_queue = Queue()
        self.parse_queue = Queue()

    def get_url(self):
        for item in range(1, 10):
            data = {'page_bypass_params': {'abtest_bypass_id': 'd850e7e257cbf85e',
                                           'params': {'caller_id': '3000010',
                                                      'channel_id': '100113',
                                                      'data_mode': 'default',
                                                      'filter_params': 'sort=75',
                                                      'page': str(item),
                                                      'page_id': 'channel_list_second_page',
                                                      'page_type': 'operation',
                                                      'platform_id': '2',
                                                      'user_mode': 'default'},
                                           'scene': 'operation'},
                    'page_context': {'page_index': str(item)},
                    'page_params': {'channel_id': '100113',
                                    'filter_params': 'sort=75',
                                    'page': str(item),
                                    'page_id': 'channel_list_second_page',
                                    'page_type': 'operation'}}
            self.url_queue.put(data)

    def get_data(self):
        while True:
            json_data = self.url_queue.get()
            # post传参  字典用json传 , 字符串用字典传
            response = requests.post(url=self.url, headers=self.headers, json=json_data, timeout=3)
            self.data_queue.put(response.json())
            self.url_queue.task_done()

    def parse_data(self):
        while True:
            data = self.data_queue.get()
            cards = data["data"]["CardList"][0]["children_list"]["list"]["cards"]
            for card in cards:
                try:
                    series_name = card["params"]["series_name"]
                    timelong = card["params"]["timelong"]
                    self.parse_queue.put({"series_name": series_name, "timelong": timelong})
                    # print({"series_name": series_name, "timelong": timelong})
                except:
                    print(card)
                    pass
            self.data_queue.task_done()

    def save_data(self):
        while True:
            data = self.parse_queue.get()
            print(data)
            global count
            count += 1
            self.parse_queue.task_done()

    def main(self):
        process_list = [multiprocessing.Process(target=self.get_url)]
        for i in range(1):
            process_list.append(multiprocessing.Process(target=self.get_data))
            process_list.append(multiprocessing.Process(target=self.parse_data))
        process_list.append(multiprocessing.Process(target=self.save_data))

        for p in process_list:
            p.daemon = True
            p.start()

        time.sleep(1)
        for q in [self.url_queue, self.data_queue, self.parse_queue]:
            q.join()


if __name__ == '__main__':
    startTime = time.time()
    tencent = TencentVideo()
    tencent.main()
    print("总耗时: ", round(time.time() - startTime, 2), "秒" + "总共爬取了", count, "条数据")
