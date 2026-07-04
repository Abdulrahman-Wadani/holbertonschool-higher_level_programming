#!/usr/bin/python3
""" Module that defines a function that reads a text file"""
import json


def save_to_json_file(my_obj, filename):
    """ Function that writes an Object to a text file,"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
