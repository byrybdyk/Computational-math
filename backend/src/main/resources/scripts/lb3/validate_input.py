import sys


def input_variables():
    left_border = float(sys.argv[3])
    right_border = float(sys.argv[4])
    inaccuracy = float(sys.argv[5])
    parts_float = float(sys.argv[6])

    if validate_borders(left_border, right_border) and validate_parts(parts_float):
        return left_border, right_border, inaccuracy, int(parts_float)


def validate_borders(left_border, right_border):
    if left_border >= right_border:
        print("The left border must be less than the right border!")
        exit()
    return True


def validate_parts(parts_float):
    try:
        parts = int(parts_float)
        if not parts_float.is_integer():
            print("The number of parts must be an integer!")
            exit()
    except ValueError:
        print("The number of parts must be an integer!")
        exit()
    if parts < 0:
        print("The number of parts must be greater than 0!")
        exit()
    return True
