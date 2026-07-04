#!/usr/bin/python3
""" Module that defines a function that reads a text file"""
import json


def load_from_json_file(filename):
    """ Function that writes an Object to a text file,"""
    with open(filename, "r") as f:
        listr = json.load(f)
        return listr
