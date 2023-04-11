class Person:
    count = 0  # 类属性，记录实例对象的个数 (存储类中 , 所有实例共享 == 全局变量)

    def __init__(self, name):
        self.name = name
        Person.count += 1

    def say_hello(self):
        print(f"Hello, my name is {self.name}.")


# 使用类属性
p1 = Person("Alice")
p2 = Person("Bob")
print(Person.count)  # 输出 2
