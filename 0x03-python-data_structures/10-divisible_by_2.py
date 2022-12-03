#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = my_list
    status = []
    for a in result:
        if a % 2 == 0 or a == 0:
            status.append(1)
        else:
            status.append(0)
    return result, status
