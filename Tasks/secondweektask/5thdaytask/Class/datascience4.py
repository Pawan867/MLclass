
class Car():
    def __init__(self, name, fuel_type):
        self.name = name
        self.fuel_type = fuel_type

    def display(self):
        print(self.name, self.engine)


class Maruti(Car):
    def __init__(self, name, fuel_type, speed):

        super().__init__(name, fuel_type)
        self.speed = speed


def travel(self):
    print(self.name, self.engine_type)


obj = Maruti("Baleno", 3)
obj.display()
obj.displayInfo()
