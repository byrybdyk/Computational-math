import sys


def input_type():
    return sys.argv[1]


def input_num_dots():
    num_dots = int(sys.argv[5])
    if int(num_dots) < 1:
        print("Incorrect value entered: number of dots must be greater than 0")
        exit()
    return num_dots


def input_borders():
    left_border = float(sys.argv[3])
    right_border = float(sys.argv[4])
    if float(left_border) >= float(right_border):
        print("Incorrect value entered: left border must be less than right border")
        exit()
    return left_border, right_border


def input_quation():
    return int(sys.argv[2])
