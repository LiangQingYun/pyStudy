# 1.类的定义
class Person:
    # self 只是个名字 , 可以改成其他名字 , 但是一般都是用 self ,其作用是一个指针 , 指向当前对象
    def __init__(self) -> object:
        self.name = '海山了'
        self.age = 18


p = Person()

print(p.name)
print(p.age)
