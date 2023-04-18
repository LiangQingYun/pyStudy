import multiprocessing
import os


def square(x):
    print("当前进程: ", os.getpid())
    return x * x


if __name__ == '__main__':
    # 创建进程池 最大进程数为4
    with multiprocessing.Pool(processes=4) as pool:
        # 通过map扁平化处理
        results = pool.map(square, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        # 打印结果
        print(results)
