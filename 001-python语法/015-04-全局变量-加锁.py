import threading
from time import sleep

g_num = 0
p_lock = threading.Lock() # 获取一个互斥锁


def run_in_thread(t_name, r_num):
    global g_num
    for i in range(r_num):
        # 添加到for里面是多线程,如果是加载for外面,则是对整个for加锁,等于单线程
        p_lock.acquire()
        g_num += 1
        p_lock.release()
    print(f"执行子线程....{t_name}  当前值{r_num}")


if __name__ == '__main__':
    t1 = threading.Thread(target=run_in_thread, args=('线程1', 1000000))
    t2 = threading.Thread(target=run_in_thread, args=('线程2', 1000000))
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(g_num)
    print("主线程执行完毕...")
