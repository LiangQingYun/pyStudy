class MyClass:
    class_attribute = 123  # 类属性

    def class_method(cls):
        print("This is a class method of MyClass.")

    @staticmethod
    def static_method():
        print("This is a static method of MyClass.")


print(dir(MyClass))  # 查看当前类的所有属性和方法
# 输出 ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__'
# , '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
# '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
# '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'class_attribute', 'class_method', 'static_method']

