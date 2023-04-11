class Calculator:
    @staticmethod  # 实际上市一个装饰器，用来标记这个方法是静态方法
    def add(a, b):
        return a + b

# 静态方法通常用于实现一些与类相关的功能，但与实例状态无关的操作。例如，我们可以使用静态方法来计算一个数的平方或立方，而不需要创建一个对象来保存该数的状态。
print(Calculator.add(1, 2))  # 输出 3
