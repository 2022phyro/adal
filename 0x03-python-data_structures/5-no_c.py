#!/usr/bin/python3
def no_c(my_string):
    my = my_string
    temp = []
    te2 = ""
    for ad in range(len(my_string)):
        if my[ad] == 'c' or my[ad] == 'C':
            pass
        else:
            temp.append(my[ad])
    print(temp)
    my_string = "".join(temp)
