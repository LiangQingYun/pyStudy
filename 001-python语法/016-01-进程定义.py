"""
    进程 = 应用
    线程 = 进程中的一个执行单元

    进程是资源分配的最小单位
    线程是程序执行的最小单位

    进程其实也不是真正的进程(非真正并发, 核数不够)，而是一个虚拟的概念
"""
import multiprocessing
import os

"""
    在 Python 中，Process 是一种用于创建进程的类。它实现了类似于线程的 API，但是可以更好地控制系统资源。
"""


def run_process(num):
    print(f"Worker {num} started , pid: {os.getpid()} ppid: {os.getppid()} ")
    from time import sleep
    sleep(1)
    print(f"Worker {num} finished , pid: {os.getpid()} ppid: {os.getppid()}")


if __name__ == "__main__":
    print("父进程pid: ", os.getpid())
    p1 = multiprocessing.Process(target=run_process, args=(1,))
    p2 = multiprocessing.Process(target=run_process, args=(2,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("所有的进程执行完毕...", os.getpid())
