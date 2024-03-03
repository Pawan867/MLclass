class Car:
    def __init__(self, tyres, doors):
        self.tyres = tyres
        self.doors = doors

    def car1(self):
        print(self.tyres, self.doors)


x = Car("suzuki", 4)
x.car1()
