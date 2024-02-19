from matrix_input import *
from gauss_method import *

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
print("Cчитана матрица:")
print_matrix(matrix)

method_Gauss(matrix)

print("Матрица после прямого хода:")
print_matrix_float(matrix)

# print("Является ли полученная матрица треугольной? ",is_triangular(matrix))
if  not is_triangular(matrix):
    print("Не получилось преобразовать матрицу к треугольному виду")
    exit()

print(reversal_method(matrix))



