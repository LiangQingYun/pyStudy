import queue
import threading
"""
task_done() 方法：该方法用于通知队列，当前任务已经完成处理。
    每次put一个任务到队列中时，内部计数器会加1，但是get()不会自动减1。所以需要手动调用task_done()方法减1。
    每次从队列中取出一个任务时，应用程序需要调用 task_done() 方法告诉队列，这个任务已经被处理完毕(计数器会减1)，队列可以继续处理下一个任务。
    否则，join() 方法会一直等待，直到 task_done() 方法被调用与之相等的次数。

join() 方法：该方法用于等待队列中所有任务的处理完成。
    当队列中的所有任务都被处理完毕后，join() 方法才会返回。也就是计数器==0的时候才会停止
    在多线程应用程序中，通常需要先调用 join() 方法等待所有任务完成，然后再停止 worker 线程。

daemon 属性：该属性用于设置线程是否为守护线程（daemon thread）。
    当一个线程为守护线程时，它会在主线程结束时自动退出，而不管它是否完成了任务。在多线程应用程序中，
    通常将 worker 线程设置为守护线程，以确保程序能够正常退出。
"""
def worker(q):
    while True:
        item = q.get()
        if item is None:
            q.task_done()
            break
        # 处理 item
        print(f"Processing {item}")
        q.task_done()

q = queue.Queue()

# 启动多个 worker 线程
for i in range(4):
    t = threading.Thread(target=worker, args=(q,))
    t.daemon = True
    t.start()

# 将任务添加到队列中
for item in range(10):
    q.put(item)

# 等待所有任务完成
q.join()

# 停止 worker 线程
for i in range(4):
    q.put(None)