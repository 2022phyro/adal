#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # for i in range(-1, (-1-len(my_list)), -1):
    for i in my_list[::-1]:
        print("{:d}".format(i))
