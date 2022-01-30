import math

#Create shape classes

class Circle:
    """A circle with a radius r"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate the area of the circle"""
        return math.pi * self.radius ** 2

    def circumference(self):
        """Calculate the circumference of the circle"""
        return 2.0 * math.pi * self.radius

    def __str__(self):
        return f"A circle with radius {self.radius}"
        
class Square:
    """A square with sides s"""

    def __init__(self, side):
        self.side = side

    def area(self):
        """Calculate the area of the square"""
        return side ** 2

    def perimeter(self):
        """Calculate the perimeter of the square"""
        return side * 4

    def __str__(self):
        return f"A square with sides {self.radius}"
