#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for ode in matrix:
        for be in ode:
            if be == ode[-1]:
                print("{}".format(be), end="\n")
            else:
                print("{}".format(be), end=" ")
