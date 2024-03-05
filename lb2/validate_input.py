

from math import cos, sin

def quation_solution(quation,x):
    if quation == 1:
        return x**2 - 3*x + 2
    elif quation == 2:
        return x**3 + 2*x**2 - 5
    elif quation == 3:
        return sin(x) - cos(x)
    else:
        print("Unknown quation")
        exit()
        

def count_roots_on_interval(quation, a, b, inaccuracy):
    b1 = b
    num_roots = 0
    x = a
    while x < b1:
        if quation_solution(quation, x) * quation_solution(quation, x + inaccuracy) < 0:
            num_roots += 1
        x += inaccuracy
    return num_roots
def validate_roots(num_roots):
    num_roots = int(num_roots)
    if num_roots <1:
        print("No roots")
        return False
    elif num_roots > 1:
        print("More than one root (", num_roots, ")")
        return False
    return True