import multiprocessing
import os

"""
    每个进程都有自己的内存空间，进程间的内存空间是相互独立的。
    因此，当一个进程修改了一个全局变量的值时，另一个进程并不会立即感知到这个变化，因为它们的内存空间并不相同。
    
    如果两个进程需要共享变量，需要使用一些特殊的机制来实现变量同步，比如使用进程间通信（IPC）机制，
    如共享内存、消息队列、管道、套接字等。这些机制可以让多个进程之间共享资源和信息，并协调它们之间的行为，从而实现进程间的同步和通信。
    
    进程如何创建 ?
        由主进程把房钱进程的代码拷贝到子进程中, 然后在子进程中执行
"""

nums = [1, 2, 3]

# 内存相互独立
def run_process(num):
    from time import sleep
    sleep(0.5)
    global nums
    nums.append(num)
    print("process - nums:", nums)

# 内存相互独立
def run_process2():
    from time import sleep
    sleep(0.5)
    global nums
    print("process2 - nums:", nums)


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=run_process, args=(4,))
    p2 = multiprocessing.Process(target=run_process2)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
