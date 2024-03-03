# Private class

class Person:
    def __init__(self, name, age):
        self._name == name
        self._age == age

    def display(self):
        print(f"the person name is {self._name} is {self._age} years old")


if __name__ == "__main__":
    person_test = Person(name="Ram", age=22)
    # print(person_test.__name)
    # print(person_test._Person__name)
    person_test.display()
