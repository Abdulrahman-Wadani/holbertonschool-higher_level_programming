#!/usr/bin/python3
""" Defines a MyList class that inherits from list."""


class MyList(list):
    """ Represents a MyList class that inherits from list."""

    def print_sorted(self):
        newlist = self[:]
        newlist.sort()
        print(newlist)
