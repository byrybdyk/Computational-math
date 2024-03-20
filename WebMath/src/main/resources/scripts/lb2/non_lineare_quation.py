import sys
from data_imput import *
from data_imput import try_to_convert_to_int
from validate_input import check_convergencecondition, converted_quation, quation_df2_solution, quation_df_solution, quation_solution

def str_quation(quation):
    if quation == 1:
        return "x^2 - 3x + 2"
    elif quation == 2:
        return "x^3 + 2x^2 - 5"
    elif quation == 3:
        return "cos(x) + x^2"

def validate_initial_approximation(quation,a,b):
    fa = quation_solution(quation,a)
    fb =  quation_solution(quation,b)
    dfa2 =quation_df2_solution(quation,a)
    dfb2 = quation_df2_solution(quation,b)

    if fa * dfa2 > 0:
        return a
    elif fb * dfb2 > 0:
        return b
    else:
        raise ValueError("No suitable initial approximation\nfound on the interval [a, b]")

def half_division_method(quation, method):
    # a, b, inaccuracy = input_selection(quation,method)
    a = try_to_convert_to_int(sys.argv[4])
    b = try_to_convert_to_int(sys.argv[5])
    inaccuracy = try_to_convert_to_int(sys.argv[6])
    
    if(float(b) - float(a) - 0.00001 < 0):
        print("The right boundary must be greater\nthan the left boundary!")
        exit()
    
    count_roots = count_roots_on_interval(quation, a, b, 0.001) 
    if not (validate_roots(count_roots)):
        exit()
        
    
    # a = int(sys.argv[4])
    # b = int(sys.argv[5])
    # inaccuracy = int(sys.argv[6])
    a1 =a
    b1 = b
    
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
    print(f"Answer = {solution}")
    print(f"f(answer) = {quation_solution(quation, solution)}")
    print(f"Iterations = {iterations}")
    # output_data(solution, quation_solution(quation, solution), iterations, str_quation(quation))
    # draw_grapth(quation, str_quation(quation), a1, b1)
    
def Newton_method(quation, method):
    a = try_to_convert_to_int(sys.argv[4])
    b = try_to_convert_to_int(sys.argv[5])
    inaccuracy = try_to_convert_to_int(sys.argv[6])
    
    if(float(b) - float(a) - 0.00001 < 0):
        print("The right boundary must be greater\nthan the left boundary!")
        exit()
    
    count_roots = count_roots_on_interval(quation, a, b, 0.001) 
    if not (validate_roots(count_roots)):
        exit()
    
    approximation = validate_initial_approximation(quation, a, b)
    
    iterations = 0
    max_iter = 1000
    x = approximation
    while abs(quation_solution(quation,x)) > inaccuracy and iterations < max_iter:
        x = x - quation_solution(quation,x) / quation_df_solution(quation,x)
        iterations += 1
        
    solution = try_to_convert_to_int(x)
    print(f"Answer = {solution}")
    print(f"f(answer) = {quation_solution(quation, solution)}")
    print(f"Iterations = {iterations}")
    
    # output_data(solution, quation_solution(quation, solution), iterations, str_quation(quation))
    # draw_grapth(quation, str_quation(quation), a, b)
    
def Simple_iteration_method(quation, method):
    # a, b, inaccuary = input_selection(quation,method)
    a = try_to_convert_to_int(sys.argv[4])
    b = try_to_convert_to_int(sys.argv[5])
    inaccuary = try_to_convert_to_int(sys.argv[6])
    
    if(float(b) - float(a) - 0.00001 < 0):
        print("The right boundary must be greater\nthan the left boundary!")
        exit()
    count_roots = count_roots_on_interval(quation, a, b, 0.001) 
    if not (validate_roots(count_roots)):
        exit()
    # lambda_L = -1/(max(abs(quation_df_solution(quation,a)), abs(quation_df_solution(quation,b))))
    # print("L = ",lambda_L)
    q = check_convergencecondition(quation, a, b)
    approximation = validate_initial_approximation(quation, a, b)
    x = approximation
    iterations = 0
    max_iter = 1000
    if q>1:
        print("The convergence condition\nis NOT met")
        exit()
    if( 0< q <= 0.5):
        while abs(converted_quation(quation,x)-x) > inaccuary and iterations < max_iter:
            x = converted_quation(quation,x)
            # print(x)
            iterations += 1
    if(0.5 <q <=1):
        while abs(converted_quation(quation,x)-x) > inaccuary and iterations < max_iter:
            x = converted_quation(quation,x)
            iterations += 1
    
    solution = try_to_convert_to_int(x)
    print(f"Answer = {solution}")
    print(f"f(answer) = {quation_solution(quation, solution)}")
    print(f"Iterations = {iterations}")
    # output_data(solution, quation_solution(quation, solution), iterations, str_quation(quation))
    # draw_grapth(quation, str_quation(quation), a, b)


def non_lineare_quation():
    quation = int(sys.argv[2])
    method = int(sys.argv[3])
    

    switch_command = {
        1: half_division_method,
        2: Newton_method,
        3: Simple_iteration_method,
        4: exit,
    }
    switch_command.get(method, exit)(quation,method)