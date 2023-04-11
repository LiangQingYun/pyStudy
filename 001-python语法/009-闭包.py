"""
内部函数引用外部函数的变量，外部函数返回内部函数的引用，这样就形成了一个闭包。
"""


def outer(x):
    def multiplier(n):
        return x * n
    return multiplier


double = outer(2)  # 创建一个闭包 double
triple = outer(3)  # 创建一个闭包 triple

print(double(5))  # 输出 10，即 2*5
print(triple(5))  # 输出 15，即 3*5
