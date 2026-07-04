#!/usr/bin/python3
""" Module that defines a function that reads a text file"""


def write_file(filename="", text=""):
    """ Writes a string to a text file and returns the number of characters"""
    with open(filename, "w") as f:
        return f.write(text)
