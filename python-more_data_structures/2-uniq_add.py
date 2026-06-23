#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    sum = 0
    for i in range(len(my_list)):
        if my_list[i] not in new_list:
            sum += my_list[i]
            new_list.append(my_list[i])
    return sum
