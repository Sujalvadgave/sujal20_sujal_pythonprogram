# Define a base class "Shape"
class Shape:
    def area(self):
        pass

# Define a derived class "Circle" that inherits from "Shape"
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Method overriding: Provide a specific implementation of the "area" method for circles
    def area(self):
        return 3.14159265358979323846 * self.radius * self.radius

# Define another derived class "Rectangle" that inherits from "Shape"
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Method overriding: Provide a specific implementation of the "area" method for rectangles
    def area(self):
        return self.width * self.height

# Create instances of the derived classes
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Calculate and print the areas of different shapes using method overriding
print(f"Area of Circle: {circle.area()}")
print(f"Area of Rectangle: {rectangle.area()}")
