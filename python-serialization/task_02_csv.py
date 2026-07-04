#!/usr/bin/python3
""" Module for serializing and deserializing using pickle """
import json
import csv


def convert_csv_to_json(filename):
    """ Converts a CSV file to JSON format """
    try:
        with open(filename, "r") as f:
            csvfile = csv.DictReader(f)
            data = list(csvfile)
        with open("data.json", "w") as jsonf:
            json.dump(data, jsonf)
        return True
    except Exception:
        return False
