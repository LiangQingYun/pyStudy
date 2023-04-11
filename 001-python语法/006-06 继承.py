# 动物类
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} is speaking.")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def wag_tail(self):
        print(f"{self.name} is wagging its tail.")


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def scratch(self):
        print(f"{self.name} is scratching.")


dog = Dog('Buddy', 'Golden Retriever')
dog.speak()  # 输出 "Buddy is speaking."
dog.wag_tail()  # 输出 "Buddy is wagging its tail."

cat = Cat('Luna', 'Black')
cat.speak()  # 输出 "Luna is speaking."
cat.scratch()  # 输出 "Luna is scratching."
