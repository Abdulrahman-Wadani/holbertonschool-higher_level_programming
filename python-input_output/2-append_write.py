#!/usr/bin/python3
""" Module that defines a function that reads a text file"""


def append_write(filename="", text=""):
    """ Writes a string to a text file and returns the number of characters"""
    with open(filename, "a") as f:
        return f.write(text)
