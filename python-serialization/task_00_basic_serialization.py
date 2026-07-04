#!/usr/bin/python3
""" Module for serializing and deserializing """
import json


def serialize_and_save_to_file(data, filename):
    """ Serializes data to a file in JSON format """
    with open(filename, "w") as f:
        json.dump(data, f)

    pass


def load_and_deserialize(filename):
    """ Loads and deserializes data from a JSON file """
    with open(filename, "r") as f:
        return json.load(f)

    pass
