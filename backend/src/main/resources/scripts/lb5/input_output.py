import sys


def input_type():
    return sys.argv[1]


def input_num_dots():
    num_dots = int(sys.argv[5])
    if int(num_dots) < 1:
        print("Incorrect value entered: number of dots must be greater than 0")
        exit()
    return num_dots


def read_dots():
    pairs = []
    try:
        for arg in sys.argv[7:8]:
            x, y = map(float, arg.replace(",", ".").split(" "))
            pair = [x, y]
            pairs.append(pair)

        for arg in sys.argv[8:]:
            if arg.strip():
                x, y = map(float, arg.replace(",", ".").split(" "))
                pair = [x, y]
                pairs.append(pair)
            else:
                continue
    except ValueError:
        print("Incorrect value entered")
        exit()
    return pairs


def input_borders():
    left_border = float(sys.argv[3])
    right_border = float(sys.argv[4])
    if float(left_border) >= float(right_border):
        print("Incorrect value entered: left border must be less than right border")
        exit()
    return left_border, right_border


def input_quation():
    return int(sys.argv[2])


def input_x():
    return float(sys.argv[6])


def read_from_file():
    pairs = []
    x = float(sys.argv[1])
    try:
        for arg in sys.argv[2:3]:
            x, y = map(float, arg.replace(",", ".").split(" "))
            pair = [x, y]
            pairs.append(pair)

        for arg in sys.argv[3:]:
            if arg.strip():
                x, y = map(float, arg.replace(",", ".").split(" "))
                pair = [x, y]
                pairs.append(pair)
            else:
                continue
    except ValueError:
        print("Incorrect value entered")
        exit()
    return pairs, x
