import os
from fractions import Fraction
from matrix_input import *
def string_multiplication(matrix, row_index, k,j):
    if row_index < 0 or row_index >= len(matrix):
        raise IndexError("Недопустимый индекс строки")
    new_row = matrix[row_index][:]

    if(not isinstance(k,int))and(k == 0):
        try:
            k = int(k)
        except ValueError:
            k = Fraction(k)
    if(not isinstance(j,int))and(j == 0):
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
        raise IndexError("Недопустимый индекс строки")
    matrix[i], matrix[j] = matrix[j], matrix[i]

def string_addition(matrix, row_index, adding_row):
    if row_index < 0 or row_index >= len(matrix):
        raise IndexError("Недопустимый индекс строки")
    for i in range(len(matrix[row_index])):
        matrix[row_index][i] += adding_row[i]
    return matrix

def method_Gauss(matrix):
    for i in range(len(matrix)):
        if (matrix[i][i] !=0):
            for j in range(i+1, len(matrix)):
                buffer_row = string_multiplication(matrix,i,matrix[j][i],matrix[i][i])
                # print("строка, на которую умножаем: ",buffer_row)
                matrix = string_addition(matrix,j,buffer_row)
                # print("изменённая строка ", matrix[j])
            
            # print_matrix(matrix)
            
        else:
            print("Обнаружен нулевой элемент")
            for p in range(i + 1, len(matrix)):
                if matrix[p][i] != 0:
                    # Меняем местами строки i и j
                    swap_rows(matrix,i,p)
                    break
                else:
                    raise ValueError("Нет ненулевого диагонального элемента")
            for j in range(i+1, len(matrix)):
                buffer_row = string_multiplication(matrix,i,matrix[j][i],matrix[i][i])
                # print("строка, на которую умножаем: ",buffer_row)
                matrix = string_addition(matrix,j,buffer_row)
                # print("изменённая строка ", matrix[j])

    return matrix


# matrix = []
# current_working_directory = os.path.dirname(__file__)
# file_path = os.path.join(current_working_directory, "1.txt")
# with open(file_path, 'r', encoding="utf-8") as file:
#     for line in file:
#         row = []
#         try:
#             row = list(map(int, line.strip().replace(",",".").split()))
#         except ValueError:
#             for item in line.strip().replace(",", ".").split():
#                 try:
#                     number_float = float(item)
#                     if number_float.is_integer(): 
#                         row.append(int(number_float)) 
#                     else:
#                         row.append(number_float) 
#                 except ValueError:
#                     row.append(float(item))
#         print(row)
#         n = len(row)
#         if (n<0)and(n>20):
#             print("Матрица в файле не явлеется квадратной")
#             # exit()
#         matrix.append(row)

def is_triangular(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            if matrix[i][j] != 0:
                return False
    return True

def reversal_method(matrix):
    n = len(matrix)
    x = [0] * n  # Создаем список для хранения решений

    for i in range(n - 1, -1, -1):  # Начинаем с последнего уравнения
        sum = 0
        for j in range(i + 1, n):  # Проходим по коэффициентам, которые выше диагонали
            sum += matrix[i][j] * x[j]
        x[i] = (matrix[i][-1] - sum) / matrix[i][i]  # Вычисляем значение переменной
    x = list(map(float, x))
    return x

# print_matrix(matrix)
# matrix = method_Gauss(matrix)
# print(is_triangular(matrix))
# print_matrix_float(matrix)
# print(reversal_method(matrix))
