import sys
import math
from sympy import symbols, limit, ln, Abs
from validate_input import input_variables


def numerical_integration():

    quation = int(sys.argv[1])
    method = int(sys.argv[2])
    left_border, right_border, inaccuracy, parts = input_variables()
    validate_integral(quation, left_border, right_border)
    switch_command = {
        1: Rectangle_method_left,
        2: Rectangle_method_centre,
        3: Rectangle_method_right,
        4: trapezoidal_method,
        5: simpson_method,
        6: exit,
    }
    switch_command.get(method, exit)(
        quation, left_border, right_border, inaccuracy, parts
    )


def Rectangle_method_left(quation, left_border, right_border, inaccuracy, parts):
    I = 99999

    while I > inaccuracy and parts < 1000000:
        i = 1
        h = (right_border - left_border) / parts
        h2 = (right_border - left_border) / (parts // 2)
        integral = 0
        integral_2 = 0

        for i in range(parts // 2):
            integral_2 += integrand(quation, left_border + (i - 1) * h2)
        integral_2 *= h2
        i = 1
        for i in range(parts):
            integral += integrand(quation, left_border + (i - 1) * h)
        integral *= h
        I = (integral_2 - integral) / (2**2 - 1)
        parts *= 2
    if integral < float("inf"):
        print(f"S = {integral}\nParts = {parts//2}\nInnacuary = {I}")
    else:
        print("The integral doesn't converge.")


def Rectangle_method_centre(quation, left_border, right_border, inaccuracy, parts):
    I = 99999

    while I > inaccuracy and parts < 1000000:
        i = 1
        h = (right_border - left_border) / parts
        h2 = (right_border - left_border) / (parts // 2)
        integral = 0
        integral_2 = 0

        for i in range(parts // 2):
            integral_2 += integrand(quation, left_border + (i - 1 + h2 / 2) * h2)
        integral_2 *= h2
        i = 1
        for i in range(parts):
            integral += integrand(quation, left_border + (i - 1 + h / 2) * h)
        integral *= h
        I = (integral_2 - integral) / (2**2 - 1)
        parts *= 2
    if integral < float("inf"):
        print(f"S = {integral}\nParts = {parts//2}\nInnacuary = {I}")
    else:
        print("The integral doesn't converge.")


def Rectangle_method_right(quation, left_border, right_border, inaccuracy, parts):
    I = 99999

    while I > inaccuracy and parts < 1000000:
        i = 1
        h = (right_border - left_border) / parts
        h2 = (right_border - left_border) / (parts // 2)
        integral = 0
        integral_2 = 0

        for i in range(parts // 2):
            integral_2 += integrand(quation, left_border + (i) * h2)
        integral_2 *= h2
        i = 1
        for i in range(parts):
            integral += integrand(quation, left_border + (i) * h)
        integral *= h
        I = (integral_2 - integral) / (2**2 - 1)
        parts *= 2
    if integral < float("inf"):
        print(f"S = {integral}\nParts = {parts//2}\nInnacuary = {I}")
    else:
        print("The integral doesn't converge.")


def trapezoidal_method(quation, left_border, right_border, inaccuracy, parts):
    I = 99999

    while I > inaccuracy and parts < 1000000:
        i = 1
        h = (right_border - left_border) / parts
        h2 = (right_border - left_border) / (parts // 2)
        integral = 0.5 * (
            integrand(quation, left_border) + integrand(quation, right_border)
        )
        integral_2 = 0.5 * (
            integrand(quation, left_border) + integrand(quation, right_border)
        )

        for i in range(parts // 2):
            integral_2 += integrand(quation, left_border + i * h2)
        integral_2 *= h2
        i = 1
        for i in range(parts):
            integral += integrand(quation, left_border + i * h)
        integral *= h
        I = (integral_2 - integral) / (2**2 - 1)
        parts *= 2
    if integral < float("inf"):
        print(f"S = {integral}\nParts = {parts//2}\nInnacuary = {I}")
    else:
        print("The integral doesn't converge.")


def simpson_method(quation, left_border, right_border, inaccuracy, parts):
    I = 99999

    while I > inaccuracy and parts < 1000000:
        # i = 1
        h = (right_border - left_border) / parts
        h2 = (right_border - left_border) / (parts // 2)
        integral = 0
        integral_2 = 0
        x_values = [left_border + i * h for i in range(parts + 1)]
        x_values_2 = [left_border + i * h2 for i in range(parts // 2 + 1)]

        integral_2 = integrand(quation, left_border) + integrand(quation, right_border)
        for i in range(1, parts // 2, 2):
            integral_2 += 4 * integrand(quation, x_values_2[i])
        for i in range(2, parts // 2 - 1, 2):
            integral_2 += 2 * integrand(quation, x_values_2[i])
        integral_2 *= h2 / 3

        integral = integrand(quation, left_border) + integrand(quation, right_border)
        for i in range(1, parts, 2):
            integral += 4 * integrand(quation, x_values[i])
        for i in range(2, parts - 1, 2):
            integral += 2 * integrand(quation, x_values[i])
        integral *= h / 3
        I = (integral_2 - integral) / (2**4 - 1)
        parts *= 2


def integrand(quation, x):
    if quation == 1:
        try:
            return 1 / x
        except ZeroDivisionError:
            print(f"Infinity breaking point at {x}")
            exit()
    if quation == 2:
        return x**2
    if quation == 3:
        return x


def validate_integral(quation, left_border, right_border):
    if quation == 1:
        x = symbols("x")
        f = ln(Abs(x))

    if quation == 2:
        x = symbols("x")
        f = (x**3) / 3
    if quation == 3:
        x = symbols("x")
        f = (x**2) / 2
    limit_value_left = limit(f, x, left_border, dir="+")
    limit_value_right = limit(f, x, right_border, dir="-")
    if limit_value_right.is_infinite or limit_value_left.is_infinite:
        print("The integral doesn't converge.")
        exit()
