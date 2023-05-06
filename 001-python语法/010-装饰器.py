import time

# 类似闭包 ,  内部函数调用外部函数的变量   外部函数返回内部函数的引用
def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {(end_time - start_time) * 1000:.2f}ms")
        return result  # 返回一个方法

    return wrapper


# 类似于java的注解
# 等同于   calculate = time_it(calculate)
@time_it
def calculate(n):
    return sum(range(n))


print(calculate(1000000))
















