from abc import ABC, abstractmethod
import math


class Shape:
    """
    Docstring for Shape
    """
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    Docstring for Circle
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return abs(self.radius * self.radius) * math.pi

    def perimeter(self):
        return math.pi * abs(self.radius) * 2


class Rectangle(Shape):
    """
    Docstring for Rectangle
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2


def shape_info(shape):
    """
    Docstring for shape_info
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
