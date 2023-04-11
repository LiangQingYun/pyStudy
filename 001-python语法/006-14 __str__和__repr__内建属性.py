class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name='{self.name}', age={self.age})"


p = Person('Alice', 25)
print(p)  # 输出: Person(name='Alice', age=25)
print(p.__str__())  # 输出: Person(name='Alice', age=25)
print(p.__repr__())  # 没有重写__repr__方法时,输出: <__main__.Person object at 0x000001F3D1B3B4C0>
