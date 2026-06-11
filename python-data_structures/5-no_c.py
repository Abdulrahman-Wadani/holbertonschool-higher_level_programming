#!/usr/bin/python3
def no_c(my_string):
    for i in range(0, len(my_string)):
        if i == 0 and (my_string[i] == "C" or my_string[i] == "c"):
            my_string = my_string[1:]
        elif i < len(my_string) and (my_string[i] == "c" or my_string[i] == "C"):
            my_string = my_string[0:i] + my_string[i + 1:]
    return my_string
