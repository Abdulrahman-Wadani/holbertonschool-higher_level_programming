#!/usr/bin/python3
def uppercase(str):
    i = 1
    for c in str:
        print("{}".format(chr(ord(c) - 32 if ord(c) >= ord('a') and ord(c)
              <= ord('z') else ord(c))),
              end="")
    print()
