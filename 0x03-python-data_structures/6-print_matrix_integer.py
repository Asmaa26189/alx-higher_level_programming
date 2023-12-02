#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) == 0:
        print("")
    else:
        for x in matrix:
            for y in x:
                print("{:d}".format(y), end=" ")
            print("")
