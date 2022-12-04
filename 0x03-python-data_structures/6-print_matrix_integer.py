#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lis in matrix:
        for mem in lis:
            if mem == lis[-1]:
                print("{:d}".format(mem))
            else:
                print("{:d}{}".format(mem, ' '), end="")
