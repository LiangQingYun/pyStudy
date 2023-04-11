class Animal:
    def make_sound(self):
        print("Generic animal sound")


class Dog(Animal):
    def make_sound(self):
        print("Bark")

# 有继承才会重写  与java类似
dog = Dog()
dog.make_sound()  # 输出: Bark
