#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for ide in matrix:
        for mad in ide:
            if mad == ide[-1]:
                print("{}".format(mad), end="")
            else:
<<<<<<< HEAD
                print("{}{}".format(mad, ' '), end="")
        print()
=======
>>>>>>> 2178c292d0f48010891794bb5d2f8652af57ce1b
