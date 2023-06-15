#!/usr/min/python3
def square_matrix_simple(matrix=[]):
    cp_matrix = matrix.copy()
    for i in range(len(matrix)):
        cp_matrix[i] = list(map(lambda x: x**2, matrix[i]))
    return cp_matrix
