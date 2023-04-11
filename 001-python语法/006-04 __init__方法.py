# 1.类的定义
class Person:
    # 构造函数 创建一个对象的时候会默认调用
    def __init__(self) -> object:
        self.name = '海山了'
        self.age = 18


p = Person()

print(p.name)
print(p.age)
