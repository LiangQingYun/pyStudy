import multiprocessing


def producer(queue):
    for i in range(10):
        queue.put(i)
    queue.put(None)  # 用None表示队列已经结束


def consumer(queue):
    while True:
        item = queue.get()
        if item is None:  # 队列结束
            break
        print(item)


"""
    队列是一种先进先出的数据结构，可以在进程之间安全地传递消息和数据。
    在Python中，使用multiprocessing.Queue可以方便地实现进程间通信。
"""
if __name__ == '__main__':
    queue = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=producer, args=(queue,))
    p2 = multiprocessing.Process(target=consumer, args=(queue,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
