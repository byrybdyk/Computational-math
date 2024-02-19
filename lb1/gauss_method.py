import os
from fractions import Fraction
from matrix_input import *

def string_multiplication(matrix, row_index, k, j):
    if row_index < 0 or row_index >= len(matrix):
        raise IndexError("Invalid row index")
    new_row = matrix[row_index][:]

    if (not isinstance(k, int)) and (k == 0):
        try:
            k = int(k)
        except ValueError:
            k = Fraction(k)
    if (not isinstance(j, int)) and (j == 0):
        try:
            j = int(j)
        except ValueError:
            j = Fraction(j)
    k = Fraction(k)
    j = Fraction(j)
    for i in range(len(new_row)):
        new_row[i] *= Fraction(-k, j)

    return new_row

def swap_rows(matrix, i, j):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix):
        raise IndexError("Invalid row index")
    matrix[i], matrix[j] = matrix[j], matrix[i]

def string_addition(matrix, row_index, adding_row):
    if row_index < 0 or row_index >= len(matrix):
        raise IndexError("Invalid row index")
    for i in range(len(matrix[row_index])):
        matrix[row_index][i] += adding_row[i]
    return matrix

def method_Gauss(matrix):
    for i in range(len(matrix)):
        if matrix[i][i] != 0:
            for j in range(i + 1, len(matrix)):
                buffer_row = string_multiplication(matrix, i, matrix[j][i], matrix[i][i])
                matrix = string_addition(matrix, j, buffer_row)
        else:
            for p in range(i + 1, len(matrix)):
                if matrix[p][i] != 0:
                    swap_rows(matrix, i, p)
                    break
                else:
                    raise ValueError("No nonzero diagonal element")
            for j in range(i + 1, len(matrix)):
                buffer_row = string_multiplication(matrix, i, matrix[j][i], matrix[i][i])
                matrix = string_addition(matrix, j, buffer_row)

    return matrix

def is_triangular(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            if matrix[i][j] != 0:
                return False
    return True

def reversal_method(matrix):
    n = len(matrix)
    x = [0] * n  # Create a list to store solutions

    for i in range(n - 1, -1, -1):  # Start from the last equation
        sum = 0
        for j in range(i + 1, n):  # Iterate over coefficients above the diagonal
            sum += matrix[i][j] * x[j]
        x[i] = (matrix[i][-1] - sum) / matrix[i][i]  # Compute the variable value
    x = list(map(float, x))
    return x

def triangular_matrix_determinant(matrix):
    det = 1
    for i in range(len(matrix)):
        det *= matrix[i][i]
    return det

def calculated_residuals(matrix, answers):
    values = []
    for row in matrix:
        sum = 0
        for j in range(len(row)-1):
            sum += row[j] * answers[j]
        values.append(row[-1] - sum)
    return values