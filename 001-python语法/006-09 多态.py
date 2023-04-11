class Animal:
    def speak(self):
        print("This is an animal speaking.")


class Dog(Animal):
    def speak(self):
        print("This is a dog barking.")


class Cat(Animal):
    def speak(self):
        print("This is a cat meowing.")


def make_animal_speak(animal):
    animal.speak()


animal1 = Animal()
animal2 = Dog()
animal3 = Cat()

make_animal_speak(animal1)  # 输出 This is an animal speaking.
make_animal_speak(animal2)  # 输出 This is a dog barking.
make_animal_speak(animal3)  # 输出 This is a cat meowing.
