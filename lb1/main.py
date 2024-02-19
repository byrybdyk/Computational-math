import os
import time
n  = 0
def hand_matrix_input():

    while True:
        try:
            n = int(input("Введите размерность матрицы, не превышающую 20\n"))
        except ValueError:
            print("Введено некорректное значение")
            continue
        if (0<=n)and(n<=20):
            break
        else:  
            print("Введено некорректное значение")
        
    print("Введено число :", n)
    time.sleep(0.5)
    matrix = []
    print("Введите матрицу. Вводите построчно, элементы разделяя пробелами")
    for i in range(n):
        while True:
            try:
                matrix_stroke = list(map(int, input(f"Введите {n} элементов для {i+1}-й строки, разделенных пробелом: ").split()))
                print(matrix_stroke)
            except ValueError:
                print("Введено некорректно число")
                continue
            except UnboundLocalError:
                print("Введено некорректно число")
                continue
            
            if len(matrix_stroke )!= n:
                print("Строка введена некорреткно")
                continue
            matrix.append(matrix_stroke)
            break
    
    
    return matrix

def is_square_matrix(matrix):
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            return False
    return True

def print_matrix(matrix):
    print("Считана матрица: ")
    for row in matrix:
        for elem in row:
            print(elem, end=" ")
        print() 

def open_file_matrix():
    current_working_directory = os.path.dirname(__file__)
    matrix = []
    while True:
        try:
            file_name = input("Введите относительный путь до вашего файла\n")
            file_path = os.path.join(current_working_directory, file_name)
            with open(file_path, 'r', encoding="utf-8") as file:
                # matrix_file = file.read()
                # print(matrix_file)
                for line in file:
                    row = list(map(int, line.strip().split()))  # Преобразование строки в список целых чисел
                    n = len(row)
                    if (n<0)and(n>20):
                        print("Матрица в файле не явлеется квадратной")
                        # exit()
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

while True:
    try:
        print("Выберите команду:")
        input_variant =int(input("1) Ввод матрицы вручную\n2) Ввод матрицы из файла\n3) Выйти из программы\n"))
        if (input_variant<=3)and(input_variant>=1): break
        print("Не существует такой команды")
        continue
    except ValueError:
        print("Введено некорректное значение")
        continue

switch_command = {
    1 : hand_matrix_input, 
    2 : open_file_matrix,
    3 : exit,
}

matrix = switch_command.get(input_variant, exit)()
print_matrix(matrix)




