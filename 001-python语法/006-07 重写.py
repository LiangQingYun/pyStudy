class Animal:
    def make_sound(self):
        print("Generic animal sound")


class Dog(Animal):
    def super_make_sound(self):
        super().make_sound()  # super()方法可以调用父类的方法


dog = Dog()
dog.make_sound()
