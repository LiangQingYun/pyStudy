class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __display(self):
        print("Name:", self.__name)
        print("Age:", self.__age)

    def get_name(self):
        return self.__name

    def set_age(self, age):
        self.__age = age

    def display_info(self):
        self.__display()


person = Person("John", 30)

# 以下两行代码会引发 AttributeError 异常
# print(person.__name)
# person.__display()

# 使用 get_name 方法获取私有属性 __name 的值
print(person.get_name())

# 使用 set_age 方法修改私有属性 __age 的值
person.set_age(31)

# 使用 display_info 方法展示所有属性的值
person.display_info()
