#!/usr/bin/python3
i = 0
for c in reversed(range(97, 123)):
    print("{}".format(chr(c) if i == 0 else chr(c - 32)), end="")
    if i == 0:
        i = 1
    else:
        i = 0
