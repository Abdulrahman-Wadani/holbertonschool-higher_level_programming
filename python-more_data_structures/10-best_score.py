#!/usr/bin/python3
def best_score(a_dictionary=dict):
    if not a_dictionary or len(a_dictionary) == 0:
        return None
    key = ""
    val = 0
    for i in a_dictionary.keys():
        if a_dictionary[i] > val:
            key = a_dictionary[i]
    return key
