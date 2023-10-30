
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

person1 = Person("Sujal", 30)
person2 = Person("Parth", 25)

person1.age = 31

person1.display_info()
person2.display_info()
