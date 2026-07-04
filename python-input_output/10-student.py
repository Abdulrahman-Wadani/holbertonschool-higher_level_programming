#!/usr/bin/python3
"""
This module defines the Student class.
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            if all(isinstance(item, str) for item in attrs):
                res = {}
                for key in attrs:
                    if key in self.__dict__:
                        res[key] = self.__dict__[key]
                return res
        return self.__dict__
