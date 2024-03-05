from data_imput import *
from validate_input import quation_solution

def str_quation(quation):
    if quation == 1:
        return "x^2 - 3x + 2"
    elif quation == 2:
        return "x^3 + 2x^2 - 5"
    elif quation == 3:
        return "sin(x) - cos(x)"

def half_division_method(quation):
    a, b, inaccuracy = input_selection(quation)
    
    
    print("a = ", a, "b = ", b, "inaccuracy = ", inaccuracy, "quation = ", quation)
    
    iterations = 0
    max_iter = 1000
    while (b - a) / 2 > inaccuracy and iterations < max_iter:
        midpoint = (a + b) / 2
        if quation_solution(quation, midpoint) == 0:
            return midpoint, iterations
        elif quation_solution(quation, a) * quation_solution(quation, midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
        iterations += 1
    if iterations >= max_iter-1:
        print("Solution not found")
        exit()
    
    solution = try_to_convert_to_int((a + b) / 2) 
    
    output_data(solution, quation_solution(quation, solution), iterations, str_quation(quation))
    
def Newton_method():
    print("Newton's method")
    
def Simple_iteration_method():
    print("Simple iteration method")
    

def non_lineare_quation():
    quation = choose_quation()
    input_variant = choose_method()
    

    switch_command = {
        1: half_division_method,
        2: Newton_method,
        3: Simple_iteration_method,
        4: exit,
    }
    switch_command.get(input_variant, exit)(quation)