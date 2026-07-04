#!/usr/bin/python3
"""
Docstring for python-input_output.7-add_item
"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file\

try:
    open("add_item.json")
except FileNotFoundError:
    existing_list = []
else:
    existing_list = load_from_json_file("add_item.json")
arg = sys.argv[1:]
existing_list.extend(arg)
save_to_json_file(existing_list, "add_item.json")
