from abc import ABC, abstractmethod


class Animal:
    """
    Docstring for Animal
    """
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """
    Docstring for Dog
    """

    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    Docstring for Cat
    """

    def sound(self):
        return "Meow"
