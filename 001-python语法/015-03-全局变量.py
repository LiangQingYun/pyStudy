"""
    全局变量
        在函数外部定义的变量，称为全局变量
        在函数内部可以使用全局变量，但是不建议使用
        如果在函数内部修改全局变量，需要使用global关键字


"""
import threading
from time import sleep

g_num = 0


def run_in_thread(t_name, r_num):
    global g_num
    for i in range(r_num):
        g_num += 1
    print(f"执行子线程....{t_name}  当前值{r_num}")


"""
    main方法是主线程
    t1和t2是子线程

    main方法相当于执行py文件 , py文件中创建两个子线程 , 主线程执行完毕后 , 子线程还在执行

    通过join方法 , 主线程等待子线程执行完毕后 , 再执行主线程
"""
if __name__ == '__main__':

    """
    run_in_thread是函数名，它本身就代表一个函数对象，不会执行函数内部的代码。
    而run_in_thread()是直接调用函数，会执行函数内部的代码。
    如果将t1 = threading.Thread(target=run_in_thread)改为t1 = threading.Thread(target=run_in_thread())，
    相当于将t1的target参数设为了run_in_thread函数的返回值，而不是函数对象本身，此时t1的执行结果是None。
    这样做会导致线程的target函数实际上并没有被执行，因此全局变量的值不会被冲突.
    """
    t1 = threading.Thread(target=run_in_thread, args=('线程1', 1000000))
    t2 = threading.Thread(target=run_in_thread, args=('线程2', 1000000))
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    """
        打印的值不对 因为在线程A累加了值,但是还未赋值的时候, 切换了线程,后面再切换到A的时候,值已经是不对的了 , 造成了数据的不一致
        
        解决方法 : 加锁
    """
    print(g_num)
    print("主线程执行完毕...")
