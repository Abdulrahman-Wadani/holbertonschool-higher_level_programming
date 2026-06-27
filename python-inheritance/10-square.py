#!/usr/bin/python3
"""
Docstring for python-inheritance.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Docstring for BaseGeometry
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
