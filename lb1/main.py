from matrix_input import *
from gauss_method import *

while True:
    try:
        print("Choose the command:")
        input_variant = int(input("1) Manual matrix input\n2) Input matrix from file\n3) Generate a random matrix\n4) Exit the program\n"))
        if input_variant in range(1, 5):
            break
        print("Invalid command")
        continue
    except ValueError:
        print("Incorrect value entered")
        continue

switch_command = {
    1: hand_matrix_input,
    2: open_file_matrix,
    3: random_matrix,
    4: exit,
}

matrix = switch_command.get(input_variant, exit)()
print("Matrix read:")
print_matrix(matrix)
first_matrix = matrix[:]

method_Gauss(matrix)

print("Matrix after forward pass:")
print_matrix_float(matrix)

if not is_triangular(matrix):
    print("Failed to transform the matrix to triangular form")
    exit()

det = triangular_matrix_determinant(matrix)
if det == 0:
    print("Determinant of the matrix = 0, cannot solve by back substitution")
    exit()
else:
    print("Determinant of the matrix = ", det, "\n")

print_answers(reversal_method(matrix))

print_residuals(calculated_residuals(first_matrix,reversal_method(matrix)))


