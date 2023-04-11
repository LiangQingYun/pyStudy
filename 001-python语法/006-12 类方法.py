class Person:
    count = 0  # 类属性

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @classmethod
    def show_count(cls):
        print("There are {} people".format(cls.count))
'''
在这个例子中，我们定义了一个类方法show_count，通过@classmethod装饰器声明，用于显示当前创建了多少个Person对象。
在show_count方法中，我们可以通过cls访问count类属性。
通过类和实例均可调用类方法，类方法和类属性都属于类本身而非实例，因此可以通过类和实例访问和修改。
'''
p1 = Person("Alice")
p2 = Person("Bob")
Person.show_count()  # 通过类调用类方法
p1.show_count()  # 通过实例调用类方法

