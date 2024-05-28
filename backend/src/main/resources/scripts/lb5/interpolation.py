from functools import reduce
from math import factorial
import numpy as np
from input_output import *
import sys


# Функции для интерполяции
def lagrange_polynomial(dots, n):
    xs = [dot[0] for dot in dots]
    ys = [dot[1] for dot in dots]
    return lambda x: sum(
        [
            ys[i]
            * reduce(
                lambda a, b: a * b,
                [(x - xs[j]) / (xs[i] - xs[j]) for j in range(n) if i != j],
            )
            for i in range(n)
        ]
    )


def divided_differences(dots):
    xs = [dot[0] for dot in dots]
    ys = [dot[1] for dot in dots]
    n = len(ys)
    coef = np.copy(ys).astype(float)
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (xs[i] - xs[i - j])
    return coef


def newton_divided_difference_polynomial(dots, n):
    xs = [dot[0] for dot in dots]
    ys = [dot[1] for dot in dots]
    coef = divided_differences(dots)
    return lambda x: ys[0] + sum(
        [
            coef[k] * reduce(lambda a, b: a * b, [x - xs[j] for j in range(k)])
            for k in range(1, n)
        ]
    )


def finite_differences(dots):
    y = [dot[1] for dot in dots]
    n = len(y)
    delta_y = np.zeros((n, n))
    delta_y[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            delta_y[i, j] = delta_y[i + 1, j - 1] - delta_y[i, j - 1]
    return delta_y


def print_finite_differences_table(delta_y):
    n = delta_y.shape[0]
    print("Finite difference table:")
    for i in range(n):
        row = [f"{delta_y[i, j]:.4f}" if i + j < n else "" for j in range(n)]
        print("\t".join(row))


def newton_finite_difference_polynomial(dots, n):
    xs = [dot[0] for dot in dots]
    ys = [dot[1] for dot in dots]
    h = xs[1] - xs[0]

    delta_y = finite_differences(dots)
    return lambda x: ys[0] + sum(
        [
            reduce(lambda a, b: a * b, [(x - xs[0]) / h - j for j in range(k)])
            * delta_y[k, 0]
            / factorial(k)
            for k in range(1, n)
        ]
    )


def gauss_polynomial(dots, n):
    xs = [dot[0] for dot in dots]
    ys = [dot[1] for dot in dots]
    n = len(xs) - 1
    alpha_ind = n // 2
    fin_difs = []
    fin_difs.append(ys[:])

    for k in range(1, n + 1):
        last = fin_difs[-1][:]
        fin_difs.append([last[i + 1] - last[i] for i in range(n - k + 1)])

    h = xs[1] - xs[0]
    dts1 = [0, -1, 1, -2, 2, -3, 3, -4, 4]

    def f1(x):
        return ys[alpha_ind] + sum(
            [
                reduce(
                    lambda a, b: a * b,
                    [
                        (x - xs[alpha_ind]) / h + dts1[j]
                        for j in range(k)
                        if j < len(dts1)
                    ],
                )
                * fin_difs[k][len(fin_difs[k]) // 2]
                / factorial(k)
                for k in range(1, min(n + 1, len(dts1)))
            ]
        )

    def f2(x):
        return ys[alpha_ind] + sum(
            [
                reduce(
                    lambda a, b: a * b,
                    [
                        (x - xs[alpha_ind]) / h - dts1[j]
                        for j in range(k)
                        if j < len(dts1)
                    ],
                )
                * fin_difs[k][len(fin_difs[k]) // 2 - (1 - len(fin_difs[k]) % 2)]
                / factorial(k)
                for k in range(1, min(n + 1, len(dts1)))
            ]
        )

    return lambda x: f1(x) if x > xs[alpha_ind] else f2(x)


def stirling_polynomial(dots, n):
    xs = [dot[0] for dot in dots]
    ys = [dot[1] for dot in dots]
    n = len(xs) - 1
    alpha_ind = n // 2
    fin_difs = []
    fin_difs.append(ys[:])

    for k in range(1, n + 1):
        last = fin_difs[-1][:]
        fin_difs.append([last[i + 1] - last[i] for i in range(n - k + 1)])

    h = xs[1] - xs[0]
    dts1 = [0, -1, 1, -2, 2, -3, 3, -4, 4]

    def f1(x):
        return ys[alpha_ind] + sum(
            [
                reduce(
                    lambda a, b: a * b,
                    [
                        (x - xs[alpha_ind]) / h + dts1[j]
                        for j in range(k)
                        if j < len(dts1)
                    ],
                )
                * fin_difs[k][len(fin_difs[k]) // 2]
                / factorial(k)
                for k in range(1, min(n + 1, len(dts1)))
            ]
        )

    def f2(x):
        return ys[alpha_ind] + sum(
            [
                reduce(
                    lambda a, b: a * b,
                    [
                        (x - xs[alpha_ind]) / h - dts1[j]
                        for j in range(k)
                        if j < len(dts1)
                    ],
                )
                * fin_difs[k][len(fin_difs[k]) // 2 - (1 - len(fin_difs[k]) % 2)]
                / factorial(k)
                for k in range(1, min(n + 1, len(dts1)))
            ]
        )

    return lambda x: (f1(x) + f2(x)) / 2


def bessel_polynomial(dots, n):
    xs = [dot[0] for dot in dots]
    ys = [dot[1] for dot in dots]
    n = len(xs) - 1
    alpha_ind = n // 2
    fin_difs = []
    fin_difs.append(ys[:])

    for k in range(1, n + 1):
        last = fin_difs[-1][:]
        fin_difs.append([last[i + 1] - last[i] for i in range(n - k + 1)])

    h = xs[1] - xs[0]
    dts1 = [0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5]

    return lambda x: (ys[alpha_ind] + ys[alpha_ind]) / 2 + sum(
        [
            reduce(
                lambda a, b: a * b,
                [(x - xs[alpha_ind]) / h + dts1[j] for j in range(k)],
            )
            * fin_difs[k][len(fin_difs[k]) // 2]
            / factorial(2 * k)
            + ((x - xs[alpha_ind]) / h - 1 / 2)
            * reduce(
                lambda a, b: a * b,
                [(x - xs[alpha_ind]) / h + dts1[j] for j in range(k)],
            )
            * fin_difs[k][len(fin_difs[k]) // 2]
            / factorial(2 * k + 1)
            for k in range(1, n + 1)
        ]
    )


# Функции для ввода и вывода данных
def interpolation():
    type_input = input_type()
    if type_input == "true":
        dots, x = interpolation_function()
    else:
        dots, x = interpolation_coordinates()

    n = len(dots)
    solve(dots, x, n)


def interpolation_from_file():
    dots = read_dots()
    for dot in dots:
        print(dot)
    n = len(dots)
    solve(dots, x, n)


def interpolation_function():
    num_dots = input_num_dots()
    left_border, right_border = input_borders()
    quation = input_quation()
    x = input_x()
    xs = np.linspace(left_border, right_border, num_dots)
    ys = []
    for x_i in xs:
        ys.append(function_solver(x_i, quation))
    dots = list(zip(xs, ys))
    return dots, x


def function_solver(x, quation):
    if quation == 1:
        return x**2 - 3 * x + 2
    elif quation == 2:
        return x**3 - 2 * x**2 - 5
    elif quation == 3:
        return x


def interpolation_coordinates():
    x = input_x()
    dots = read_dots()
    return dots, x


# Основная функция решения
def solve(dots, x, n):
    delta_y = finite_differences(dots)
    print_finite_differences_table(delta_y)

    methods = [
        ("Lagrange polynomial", lagrange_polynomial),
        (
            "Newton polynomial with divided differences",
            newton_divided_difference_polynomial,
        ),
        (
            "Newton polynomial with finite differences",
            newton_finite_difference_polynomial,
        ),
        ("Gauss polynomial", gauss_polynomial),
        ("Stirling polynomial", stirling_polynomial),
        ("Bessel polynomial", bessel_polynomial),
    ]

    xs = [dot[0] for dot in dots]
    ys = [dot[1] for dot in dots]

    for name, method in methods:
        finite_difference = True
        last = xs[1] - xs[0]
        for i in range(1, n):
            new = abs(xs[i] - xs[i - 1])
            if abs(new - last) > 0.0001:
                finite_difference = False
            last = new

        if (method is newton_finite_difference_polynomial) and not finite_difference:
            continue

        if (method is newton_divided_difference_polynomial) and finite_difference:
            continue

        if (method is gauss_polynomial or method is stirling_polynomial) and len(
            xs
        ) % 2 == 0:
            continue

        if method is bessel_polynomial and len(xs) % 2 == 1:
            continue

        h = xs[1] - xs[0]
        alpha_ind = n // 2
        t = (x - xs[alpha_ind]) / h
        print("t: ", t)

        print(name)
        P = method(dots, n)
        print(f"P({x}) = {P(x)}")
        print()
