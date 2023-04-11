# 迭代器
class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.a = 0
        self.b = 1
        self.count = 0

    def __add__(self, other):
        self.n = self.n + other

    ''''
    这个方法表示这是一个可迭代的对象 
    '''

    def __iter__(self):
        return self

    ''''
    返回序列中的下一个元素。当没有下一个元素时，抛出 StopIteration 异常。
    '''
    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return result

fib = Fibonacci(9)
fib.__add__(1)
for i in fib:
    print(i)
