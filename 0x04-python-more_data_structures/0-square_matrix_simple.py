#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    # for i in range(0,len(matrix)):
    #     created_list = []
    #     for j in range(0,len(matrix[i])):
    #         created_list.append(matrix[i][j] * matrix[i][j])
    #     new_matrix.append(created_list)
    # return new_matrix
    new_matrix = [list(map (lambda x : x * x, row)) for row in matrix] 
    return new_matrix
    # return ([list(map(lambda x: x * x, row)) for row in matrix])
