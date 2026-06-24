#!/usr/bin/python3
def raise_exception_msg(message=""):
    raise_exception_msg(NameError, message)


try:
    raise_exception_msg("C is fun")
except NameError as ne:
    print(ne)
