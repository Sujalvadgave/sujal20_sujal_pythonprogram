
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def get_info(self):
        return f"Brand: {self.brand}, Model: {self.model}"

class Car(Vehicle):
    def __init__(self, brand, model, color):
        super().__init__(brand, model)
        self.color = color

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Color: {self.color}"
my_car = Car("Toyota", "Camry", "Blue")

print("Car Information:")
print(my_car.get_info())
