import threading
from time import sleep


def run_in_thread():
    sleep(3)
    print("执行子线程....")


"""
    main方法是主线程
    t1和t2是子线程
    
    main方法相当于执行py文件 , py文件中创建两个子线程 , 主线程执行完毕后 , 子线程还在执行
    
    通过join方法 , 主线程等待子线程执行完毕后 , 再执行主线程
"""
if __name__ == '__main__':
    t1 = threading.Thread(target=run_in_thread)
    t2 = threading.Thread(target=run_in_thread)
    t1.start()
    t2.start()

    # t1.join()
    # t2.join()

    # 此方法替代上面两行代码(原生)
    while True:
        print("主线程执行中...")
        sleep(1)
        if threading.enumerate().__len__() <= 1:
            print("子线程执行完毕...")
            break
    print("主线程执行完毕...")
