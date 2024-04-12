import sys
import numpy as np
from data_imput import try_to_convert_to_int
def non_lineare_system():
    system_num = int (sys.argv[2])
    method = int(sys.argv[3])
    

    switch_command = {
        1: simple_iteration_method,
        2: exit,
    }
    switch_command.get(method, exit)(system_num,method)
    
def simple_iteration_method(system,method) :
    x0 = try_to_convert_to_int(sys.argv[4])
    y0 = try_to_convert_to_int(sys.argv[5])
    inaccuracy = try_to_convert_to_int(sys.argv[6])
    max_iter = 1000
    iteration =0
    if not check_convergence(system, method, x0, y0):
        print("The iteration matrix does not\nsatisfy the convergence condition.")
        exit()
    
    for i in range(max_iter):
        x = f1(x0, y0,system)
        y = f2(x0, y0,system)
        if (abs(x-x0)< inaccuracy)and(abs(y-y0)< inaccuracy):
            print(f"x = {x}\ny = {y}")
            # print(f"")
            print(f"Iterations = {iteration}")
            print(f"inncuary x= {x-f1(x,y,system)}\ninnacuary y= {y-f2(x,y,system)}")
            return x, y
        x0, y0 = x, y
        iteration += 1
    print("НЕ сходится")
def f1(x,y,system):
    if(system == 1):
        return 0.3 - 0.1*x*x- 0.2*y*y
    elif(system == 2):
        return 3*y*y+0.5*x*x
    else: 
        print("System out of choice")
        exit()
def f2(x,y,system):
    if(system == 1):
        return 0.7 -0.2*x*x - 0.1*x*y
    elif(system == 2):
        return np.sin(x)**2
    else:
        print("System out of choice")
        exit()
def check_convergence(system, method, x0, y0):
    jacobian_matrix = np.array([[f1_dx(system, x0, y0), f1_dy(system, x0, y0)], 
                                [f2_dx(system, x0, y0), f2_dy(system, x0, y0)]])
    eigenvalues = np.linalg.eigvals(jacobian_matrix)
    if np.all(np.abs(eigenvalues) < 1):
        return True
    else:
        return False

def f1_dx(system, x, y):
    if system == 1:
        return -0.2 * x
    elif system == 2:
        return x
    else:
        print("System out of choice")
        exit()

def f1_dy(system, x, y):
    if system == 1:
        return -0.4 * y
    elif system == 2:
        return 6*y
    else:
        print("System out of choice")
        exit()

def f2_dx(system, x, y):
    if system == 1:
        return -0.4 * x - 0.1 * y
    elif system == 2:
        return np.sin(2*x)
    else:
        print("System out of choice")
        exit()

def f2_dy(system, x, y):
    if system == 1:
        return 0
    elif system == 2:
        return 0
    else:
        print("System out of choice")
        exit()
