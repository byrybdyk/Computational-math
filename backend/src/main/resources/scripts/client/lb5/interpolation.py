from functools import reduce
from math import factorial
import numpy as np
from input_output import *


def interpolation():
    dots, x = inpit_pairs_selection()

    n = len(dots)
    solve(dots, x, n)


def lagrange_polynomial(xs, ys, n):
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


def divided_differences(x, y):
    n = len(y)
    coef = np.copy(y).astype(float)
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (x[i] - x[i - j])
    return coef


def newton_divided_difference_polynomial(xs, ys, n):
    coef = divided_differences(xs, ys)
    return lambda x: ys[0] + sum(
        [
            coef[k] * reduce(lambda a, b: a * b, [x - xs[j] for j in range(k)])
            for k in range(1, n)
        ]
    )


def finite_differences(y):
    n = len(y)
    delta_y = np.zeros((n, n))
    delta_y[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            delta_y[i, j] = delta_y[i + 1, j - 1] - delta_y[i, j - 1]
    return delta_y


def newton_finite_difference_polynomial(xs, ys, n_temp):
    n = len(xs)
    divided_diffs = [[0] * n for _ in range(n)]
    for i in range(n):
        divided_diffs[i][0] = ys[i]
    for j in range(1, n):
        for i in range(n - j):
            divided_diffs[i][j] = (
                divided_diffs[i + 1][j - 1] - divided_diffs[i][j - 1]
            ) / (xs[i + j] - xs[i])

    def interpolation_polynomial(x):
        result = divided_diffs[0][0]
        temp = 1
        for i in range(1, n):
            temp *= x - xs[i - 1]
            result += divided_diffs[0][i] * temp
        return result

    return interpolation_polynomial


def print_finite_differences_table(delta_y):
    n = delta_y.shape[0]
    print("Finite difference table:")
    for i in range(n):
        row = [f"{delta_y[i, j]:.4f}" if i + j < n else "" for j in range(n)]
        print("\t".join(row))


def gauss_polynomial(xs, ys, n):
    n = len(xs) - 1
    alpha_ind = n // 2
    fin_difs = []
    fin_difs.append(ys[:])

    for k in range(1, n + 1):
        last = fin_difs[-1][:]
        fin_difs.append([last[i + 1] - last[i] for i in range(n - k + 1)])

    h = xs[1] - xs[0]
    dts1 = [0, -1, 1, -2, 2, -3, 3, -4, 4]

    f1 = lambda x: ys[alpha_ind] + sum(
        [
            reduce(
                lambda a, b: a * b,
                [(x - xs[alpha_ind]) / h + dts1[j] for j in range(min(k, len(dts1)))],
            )
            * fin_difs[k][len(fin_difs[k]) // 2]
            / factorial(k)
            for k in range(1, n + 1)
        ]
    )

    f2 = lambda x: ys[alpha_ind] + sum(
        [
            reduce(
                lambda a, b: a * b,
                [(x - xs[alpha_ind]) / h - dts1[j] for j in range(min(k, len(dts1)))],
            )
            * fin_difs[k][len(fin_difs[k]) // 2 - (1 - len(fin_difs[k]) % 2)]
            / factorial(k)
            for k in range(1, n + 1)
        ]
    )

    return lambda x: f1(x) if x > xs[alpha_ind] else f2(x)


def stirling_polynomial(xs, ys, n):
    n = len(xs) - 1
    alpha_ind = n // 2
    fin_difs = []
    fin_difs.append(ys[:])

    for k in range(1, n + 1):
        last = fin_difs[-1][:]
        fin_difs.append([last[i + 1] - last[i] for i in range(n - k + 1)])

    h = xs[1] - xs[0]
    dts1 = [0, -1, 1, -2, 2, -3, 3, -4, 4]

    f1 = lambda x: ys[alpha_ind] + sum(
        [
            reduce(
                lambda a, b: a * b,
                [(x - xs[alpha_ind]) / h + dts1[j] for j in range(min(k, len(dts1)))],
            )
            * fin_difs[k][len(fin_difs[k]) // 2]
            / factorial(k)
            for k in range(1, n + 1)
        ]
    )

    f2 = lambda x: ys[alpha_ind] + sum(
        [
            reduce(
                lambda a, b: a * b,
                [(x - xs[alpha_ind]) / h - dts1[j] for j in range(min(k, len(dts1)))],
            )
            * fin_difs[k][len(fin_difs[k]) // 2 - (1 - len(fin_difs[k]) % 2)]
            / factorial(k)
            for k in range(1, n + 1)
        ]
    )

    return lambda x: (f1(x) + f2(x)) / 2


def bessel_polynomial(xs, ys, n_temp):
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


def solve(dots, x, n):
    xs = [dot[0] for dot in dots]
    ys = [dot[1] for dot in dots]
    delta_y = finite_differences(ys)
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
        P = method(xs, ys, n)
        print(f"P({x}) = {P(x)}\n")

        plot(name, xs, ys, P, x)
