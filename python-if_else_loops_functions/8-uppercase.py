#!/usr/bin/python3
def uppercase(str):
    i = 1
    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            print("{}".format(chr(ord(c) - 32)),
                  end="" if i != len(str) else "\n")
        else:
            print("{}".format(c), end="" if i != len(str) else "\n")
        i += 1
