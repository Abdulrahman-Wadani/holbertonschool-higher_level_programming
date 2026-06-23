#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new = sorted(dict.keys(a_dictionary))
    for i in new:
        print(i, dict.get(a_dictionary, i), sep=": ")
