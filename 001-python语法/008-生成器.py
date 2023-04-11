# yield

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
print(next(fib)) # 输出 0
print(next(fib)) # 输出 1
print(next(fib)) # 输出 1
print(next(fib)) # 输出 2
print(next(fib)) # 输出 3
