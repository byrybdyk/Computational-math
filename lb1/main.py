from matrix_input import *
from gauss_method import *

while True:
    try:
        print("Выберите команду:")
        input_variant =int(input("1) Ввод матрицы вручную\n2) Ввод матрицы из файла\n3) Создать случайную мтарицу\n4) Выйти из программы\n"))
        if (input_variant<=3)and(input_variant>=1): break
        print("Не существует такой команды")
        continue
    except ValueError:
        print("Введено некорректное значение")
        continue

switch_command = {
    1 : hand_matrix_input, 
    2 : open_file_matrix,
    3 : random_matrix,
    4 : exit,
}

matrix = switch_command.get(input_variant, exit)()
print("Cчитана матрица:")
print_matrix(matrix)

method_Gauss(matrix)

print("Матрица после прямого хода:")
print_matrix_float(matrix)

if  not is_triangular(matrix):
    print("Не получилось преобразовать матрицу к треугольному виду")
    exit()

det = triangular_matrix_determinant(matrix)
if det == 0:
    print("Детерминант матрицы = 0, решить обратным ходом невозможно")
    exit()
else:
    print("Детерминант матрицы = ",det,"\n")


print_answers(reversal_method(matrix))



