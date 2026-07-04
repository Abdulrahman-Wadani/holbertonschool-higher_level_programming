#!/usr/bin/python3
""" Module that defines a function that reads a text file"""
import json
""" Module that defines a function that reads a text file"""


def to_json_string(my_obj):
    """ Writes a string to a text file and returns the number of characters"""
    return json.dumps(my_obj)
