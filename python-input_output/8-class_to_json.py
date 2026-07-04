#!/usr/bin/python3
""" Module that defines a function that converts a class"""


def class_to_json(obj):
    """ Function that returns the dictionary description with"""
    return obj.__dict__
