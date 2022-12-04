#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for ide in matrix:
        for mad in ide:
            if mad == ide[-1]:
                print("{}".format(mad))
            else:
                print("{}{}".format(mad, ' '), end="")
