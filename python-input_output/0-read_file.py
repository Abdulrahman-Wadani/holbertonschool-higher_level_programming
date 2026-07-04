#!/usr/bin/python3
""" Module that defines a function that reads a text file"""


def read_file(filename=""):
    """ Reads a text file and prints it to stdout """
    with open(filename) as f:
        print(f.read(), end="")
