#!/usr/bin/python3
""" Module that defines a function that returns the list of"""


class BaseGeometry:
    """ Returns True if the object is an instance of a class that"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
