#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return "None"
    v = 0
    for ma in range(len(my_list)):
        if my_list[ma] >= v:
            v = my_list[ma]
    return v
