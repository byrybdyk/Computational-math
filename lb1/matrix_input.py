import os
import random

def hand_matrix_input():
    while True:
        try:
            n = int(input("Enter the dimension of the matrix, not exceeding 20\n"))
        except ValueError:
            print("Incorrect value entered")
            continue
        if 0 <= n <= 20:
            break
        else:  
            print("Incorrect value entered (Matrix must be from 0 to 20)")

    print("Entered number:", n)
    matrix = []
    print("Enter the matrix. Enter row by row, separating elements by spaces")
    for i in range(n):
        while True:
            row = []
            try:
                matrix_row = input(f"Enter {n+1} elements for the {i + 1}-th row, separated by spaces: ").replace(",", ".").split()
                row = list(map(int, matrix_row))
            except ValueError:
                for item in matrix_row:
                    try:
                        number_float = float(item)
                        if number_float.is_integer(): 
                            row.append(int(number_float)) 
                        else:
                            row.append(number_float) 
                    except ValueError:
                        if(isinstance(item, float)):
                            row.append(float(item))
                        else:
                            print("Incorrect number entered")
                            continue
                
            except UnboundLocalError:
                print("Incorrect number entered")
                continue
            
            if len(row) != n + 1:
                print("The row was entered incorrectly")
                continue
            matrix.append(row)
            break
    
    return matrix

def is_square_matrix(matrix):
    n = len(matrix)
    for row in matrix:
        if len(row) != n + 1:
            return False
    return True

def print_matrix(matrix):
    for row in matrix:
        for i, elem in enumerate(row):
            if i == len(row) - 1:
                print("|", end=" ")
            print(elem, end=" ")
        print()
    print()

def print_matrix_float(matrix):
    for row in matrix:
        for i, elem in enumerate(row):
            if i == len(row) - 1:
                print("|", end=" ")
            print(float(elem), end=" ") 
        print()
    print()

def open_file_matrix():
    current_working_directory = os.path.dirname(__file__)
    matrix = []
    while True:
        try:
            file_name = input("Enter the relative path to your file\n")
            print()
            file_path = os.path.join(current_working_directory, file_name)
            with open(file_path, 'r', encoding="utf-8") as file:
                for line in file:
                    row = []
                    try:
                        row = list(map(int, line.strip().replace(",", ".").split()))
                    except ValueError:
                        for item in line.strip().replace(",", ".").split():
                            try:
                                number_float = float(item)
                                if number_float.is_integer(): 
                                    row.append(int(number_float)) 
                                else:
                                    row.append(number_float) 
                            except ValueError:
                                row.append(float(item))
                    matrix.append(row)
                break
        except FileNotFoundError:
            print("Incorrect file path entered")
            continue
        except ValueError:
            print("Incorrect coefficients in the specified file")
            exit()
    if not is_square_matrix(matrix):
        print("The matrix in the file is not square")
        exit()
    return matrix

def print_answers(row):
    answer = ""
    for elem in range(len(row)):
        answer += "x" + str(elem + 1) + " = " + str(row[elem]) + "  "
    print(answer)

def print_residuals(residuales):
    answer = ""
    for elem in range(len(residuales)):
        answer += "r" + str(elem + 1) + " = " + str(residuales[elem]) + "  "
    print(answer)

def random_matrix():
    while True:
        try:
            n = int(input("Enter the dimension of the matrix, not exceeding 20\n"))
        except ValueError:
            print("Incorrect value entered")
            continue
        if 0 <= n <= 20:
            break
        else:  
            print("Incorrect value entered (Matrix must be from 0 to 20)")
    matrix = []
    for i in range(n):
        row =[]
        for i in range(n + 1):
            if random.random() < 0.5:
                row.append(random.randint(-10, 100))
            else:
                row.append(random.uniform(-10, 100))

        matrix.append(row)
    return matrix
