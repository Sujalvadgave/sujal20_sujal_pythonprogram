
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def get_info(self):
        return f"Vehicle: Brand - {self.brand}, Model - {self.model}"


class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type

    def engine_info(self):
        return f"Engine: Fuel Type - {self.fuel_type}"


class Car(Vehicle, Engine):
    def __init__(self, brand, model, fuel_type, color):
        
        Vehicle.__init__(self, brand, model)
        Engine.__init__(self, fuel_type)
        self.color = color

    def get_info(self):
        vehicle_info = Vehicle.get_info(self)
        engine_info = Engine.engine_info(self)
        return f"{vehicle_info}, {engine_info}, Color - {self.color}"

my_car = Car("Toyota", "Camry", "Gasoline", "Blue")

print("Car Information:")
print(my_car.get_info())
