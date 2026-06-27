#!/usr/bin/python3
""" Module that defines a function that returns the list of"""


def lookup(obj):
    """ Returns the list of available attributes and methods of an object."""
    return dir(obj)


class MyClass1(object):
    pass


class MyClass2(object):
    my_attr1 = 3

    def my_meth(self):
        pass
