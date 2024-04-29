from valida_input import validate_pairs
from output import print_linear


def approximation():
    pairs = validate_pairs()
    linear_answer = linear_approximation(pairs)
    print_linear(linear_answer)


def linear_approximation(pairs):
    s_x = 0
    s_y = 0
    s_xx = 0
    s_xy = 0
    for pair in pairs:
        x = pair[0]
        y = pair[1]
        s_x += x
        s_y += y
        s_xx += x * x
        s_xy += x * y
    x_svg = s_x / len(pairs)
    y_svg = s_y / len(pairs)
    b = (s_y - s_x * s_xy / s_xx) / (len(pairs) - s_x * s_x / s_xx)
    a = (s_xy - s_x * b) / s_xx

    compare = []
    fi = []
    pi = []
    compare_sqr = 0
    for pair in pairs:
        temp = a * pair[0] + b
        fi.append(temp)
        e = temp - pair[1]
        temp2 = e / pair[1]
        pi.append(temp2)
        compare.append(e)
        compare_sqr += e * e
    tmp_top = 0
    tmp_bottom_left = 0
    tmp_bottom_right = 0
    for pair in pairs:
        tmp_top += (pair[0] - x_svg) * (pair[1] - y_svg)
        tmp_bottom_left += (pair[0] - x_svg) ** 2
        tmp_bottom_right += (pair[1] - y_svg) ** 2
    pirson = tmp_top / (tmp_bottom_left * tmp_bottom_right) ** 0.5
    # print(f"P1(x) = {a}x + {b}\nS = {compare_sqr} Pirson = {pirson}")
    return [compare_sqr, f"P1(x) = {a}x + {b}", fi, compare, pirson, pi]
