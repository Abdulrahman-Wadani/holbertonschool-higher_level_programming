#!/usr/bin/python3
def remove_char_at(str, n):
    s = str[1]
    for i in range(2, len(str)):
        if i != n + 1:
            s += str[i]
    print(s)
