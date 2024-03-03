from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self): pass

    @abstractmethod
    def move(self): pass

    @abstractmethod
    def eat(self): pass


class Mammal(Animal):
    def move(self): print("Moving on land")


class Bird(Animal):
    def move(self): print("Flying in the sky")


class Fish(Animal):
    def move(self): print("Swimming in water")


class Dog(Mammal):
    def speak(self): print("Bark")
    def eat(self): print("Eating meat")


class Cat(Mammal):
    def speak(self): print("Meow")
    def eat(self): print("Eating fish")


class Eagle(Bird):
    def speak(self): print("Scream")
    def eat(self): print("Eating fish")


class Penguin(Bird):
    def speak(self): print("Squawk")
    def eat(self): print("Eating fish")
    def swim(self): print("Swimming")


class Salmon(Fish):
    def speak(self): print("...")
    def eat(self): print("Eating smaller fish")


class Goldfish(Fish):
    def speak(self): print("...")
    def eat(self): print("Eating fish food")


for animal in [Dog(), Cat(), Eagle(), Penguin(), Salmon(), Goldfish()]:
    print(f"\n{animal.__class__.__name__}:")
    animal.speak()
    animal.move()
    animal.eat()
    if isinstance(animal, Penguin):
        animal.swim()
