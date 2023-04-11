"""
进程是程序执行时的一个实例。每个进程都是独立的，拥有自己独立的内存空间，包括代码、数据和栈等。进程之间不能直接共享数据，通信需要借助于进程间通信(IPC)机制。

线程是进程中执行的一个实体，是进程中的一个执行路径。同一个进程中的线程可以共享进程的内存空间。线程之间可以直接访问共享变量，可以通过加锁机制实现对共享变量的互斥访问。

因为线程可以共享进程的内存空间，所以在创建和销毁、切换等方面的开销比进程小，多线程编程的开发效率比多进程更高。但是，线程之间共享进程的内存空间也带来了一些安全问题，如竞态条件、死锁等问题。

因此，在使用多线程时需要注意线程安全问题，保证多个线程访问共享资源时的正确性和并发性

单核是轮流执行，多核是同时执行
"""

import threading
from datetime import time
from time import sleep


def worker(num):
    """这是线程要执行的函数"""
    sleep(5)
    print(f"Thread {num} is running")


if __name__ == "__main__":
    # 创建5个线程
    threads = []
    for i in range(10):
        # 传递worker函数的引用进去
        t = threading.Thread(target=worker, args=(i,))
        """
        .start类似于以下代码 :
        class threading():
            def start(self):
                worker()
        """
        t.start()

    print("All threads are done")
