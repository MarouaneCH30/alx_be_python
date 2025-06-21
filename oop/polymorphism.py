
from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    def area(self):
        pi = 3.14
        return pi * self.radius **2

class Square(Shape):
    def __init__(self, side):
        super().__init__()
        self.side = side
    
    def area(self):
        return self.side **2
        
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

shapes = [Circle(7), Square(10), Rectangle(20, 10)]

for shape in shapes:
    print(shape.area())