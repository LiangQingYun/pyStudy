"""
self 只是个名字 , 可以改成其他名字 , 但是一般都是用 self ,其作用是一个指针 , 指向当前对象

python中 __表示私有属性,私有方法,私有类
"""


class Person:
    # 类属性
    country = 'China'

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__money = 1000  # 私有属性

    def set_money(self, money):  # 私有属性对外提供的方法
        self.__money = money

    def get_money(self):
        return self.__money

    def __bank_2_bank(self):  # 私有方法
        print('转账成功')

    def introduce(self):
        print(f"My name is {self.name} and I'm {self.age} years old.")


p = Person('海山了', 18)
p.sex = '男'  # 动态添加属性
p.introduce()
# p.__bank_2_bank()  # 私有方法外部无法调用
# p.__money = 100000  # 私有属性外部无法调用
print(p.__str__())


# 继承
class Student(Person):
    def __init__(self, name, age, score):
        super().__init__(name, age)
        self.score = score
        # self.name = name
        # self.age = age


    def introduce(self):
        print(f"My name is {self.name} and I'm {self.age} years old. I got {self.score} in the exam.")

Student('海山了', 18, 100).introduce()


