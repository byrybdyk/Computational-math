import os
import random
n  = 0
def hand_matrix_input(): # Ручной ввод матрицы

    while True:
        try:
            n = int(input("Введите размерность матрицы, не превышающую 20\n"))
        except ValueError:
            print("Введено некорректное значение")
            continue
        if (0<=n)and(n<=20):
            break
        else:  
            print("Введено некорректное значение(Матрица должнабыть от 0 до 20)")
        
    print("Введено число :", n)
    matrix = []
    print("Введите матрицу. Вводите построчно, элементы разделяя пробелами")
    for i in range(n):
        while True:
            try:
                matrix_stroke = list(map(int, input(f"Введите {n} элементов для {i+1}-й строки, разделенных пробелом: ").replace(",",".").split()))
                # print(matrix_stroke)
            except ValueError:
                print("Введено некорректно число")
                continue
            except UnboundLocalError:
                print("Введено некорректно число")
                continue
            
            if len(matrix_stroke )!= n+1:
                print("Строка введена некорреткно")
                continue
            matrix.append(matrix_stroke)
            break
    
    
    return matrix

def is_square_matrix(matrix):
    n = len(matrix)
    for row in matrix:
        if len(row) != n+1:
            return False
    return True

def print_matrix(matrix):
    for row in matrix:
        for i,elem in enumerate(row):
            if(i== len(row)-1):
                print("|", end=" ")
            print(elem, end=" ")
        print()
    print()
def print_matrix_float(matrix):
    for row in matrix:
        for i,elem in enumerate(row):
            if(i== len(row)-1):
                print("|", end=" ")
            print(float(elem), end=" ") 
        print()
    print()

def open_file_matrix():
    current_working_directory = os.path.dirname(__file__)
    matrix = []
    while True:
        try:
            file_name = input("Введите относительный путь до вашего файла\n")
            print()
            file_path = os.path.join(current_working_directory, file_name)
            with open(file_path, 'r', encoding="utf-8") as file:
                for line in file:
                    row = []
                    try:
                        row = list(map(int, line.strip().replace(",",".").split()))
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
            print("Введён неправильный путь к файлу")
            continue
        except ValueError:
            print("Некорректные коэффициенты в указанном файле")
            exit()
    if (not is_square_matrix(matrix)):
        print("Матрица в файле не явлеется квадратной")
        exit()
    return matrix
def print_answers(row):
    answer = ""
    for elem in range(len(row)):
        answer += "x" + str(elem+1) + " = " + str(row[elem])+"  "
    print(answer)

def random_matrix():
    while True:
        try:
            n = int(input("Введите размерность матрицы, не превышающую 20\n"))
        except ValueError:
            print("Введено некорректное значение")
            continue
        if (0<=n)and(n<=20):
            break
        else:  
            print("Введено некорректное значение(Матрица должнабыть от 0 до 20)")
    matrix = []
    for i in range(n):
        row =[]
        for i in range(n+1):
            if random.random() < 0.5:
                row.append(random.randint(-10, 100))
            else:
                row.append(random.uniform(-10, 100))

        matrix.append(row)
    return matrix   