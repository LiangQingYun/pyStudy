# 1.类的定义
class Person:
    # init 类似构造函数   给了默认值
    # __方法__  是python的魔法方法
    def __init__(self) -> object:
        self.name = '海山了'
        self.age = 18


p = Person()

print(p.name)
print(p.age)
