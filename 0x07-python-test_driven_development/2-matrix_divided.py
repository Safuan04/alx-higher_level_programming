#!/usr/bin/python3

def matrix_divided(matrix, div):
    """divides all elements of a matrix"""
    new_matrix = matrix.copy()

    if not isinstance(matrix, list) or not all(
            isinstance(row, list) and all(
                isinstance(element, (int, float)) for element in row)
            for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_len = len(matrix[0])

    for row in matrix:
        if not row_len == len(row):
            raise TypeError("Each row of the matrix must have the same size")

    for i in range(len(new_matrix)):
        new_matrix[i] = list(
            map(lambda element: round(element / div, 2), matrix[i]))

    return new_matrix
