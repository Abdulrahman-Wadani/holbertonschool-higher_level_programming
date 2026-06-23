#!/usr/bin/python3
def multiply_by_2(a_dictionary=dict):
    a_dictionary = a_dictionary.copy()
    key = a_dictionary.keys()
    for i in key:
        a_dictionary[i] = a_dictionary[i] * 2
    return a_dictionary
