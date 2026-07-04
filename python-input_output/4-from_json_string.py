#!/usr/bin/python3
""" Module that defines a function that reads a text file"""
import json


def from_json_string(my_str):
    """ Writes a string to a text file and returns the number of characters"""
    return json.loads(my_str)
