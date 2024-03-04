# Program to calculate circle
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def getArea(self):
        area = math.pi * self.radius ** 2
        return area
    
    def getCircumference(self):
        circumference = 2 * math.pi * self.radius
        return circumference

# Test the Circle class
circle1 = Circle(2)
print("Circle with radius 2:")
print("Area:", circle1.getArea())
print("Circumference:", circle1.getCircumference())

circle2 = Circle(5)
print("\nCircle with radius 5:")
print("Area:", circle2.getArea())
print("Circumference:", circle2.getCircumference())
