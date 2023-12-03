#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
                element =matrix[x][y]
                print("{:d}".format(element), end="")
                if y != (len(matrix[x]) - 1):
                    print(" ", end="")

        print("")
