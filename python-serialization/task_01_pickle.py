#!/usr/bin/python3
""" Module for serializing and deserializing using pickle """
import pickle


class CustomObject:
    """ Represents a custom object with name, age, and is_student"""
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(
            f"Name: {self.name}\nAge: {self.age}\nis Student: {self.is_student}")

    def serialize(self, filename):
        try: 
            with open(filename, "wb") as f:
                pickle.dump(self, f)
            pass
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
            pass
        except Exception:
            return None
