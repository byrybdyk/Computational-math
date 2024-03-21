import math


a = float(1)
b = float(1.5)
epsilon = float(0.05)
quation_name = "x^2 - 2x + e^(-x)"

def calculate_question(x):
    return x*x - 2*x + math.exp(-x)

def df_dx(x):
    return 2*x - 2 - math.exp(-x)

def df2_dx2(x):
    return 2 + math.exp(-x)

def half_hord(a,b, epsilon):
    
    for i in range(25):
        x1 = (b + a - epsilon)/2
        x2 = (b + a + epsilon)/2
        
        if calculate_question(x1) <= calculate_question(x2):
            b = x2
            print(f"Итерация {i+1}, a = {a}, b = {b}, epsilon_n = {(b-a)/2}, x1 = {round(x1, 5)}, x2 = {round( x2, 5)}, f(x1) = {round(calculate_question(x1),5)}, f(x2) = {round(calculate_question(x2),5)}, f(x1) <= f(x2)")
        else:
            a = x1
            print(f"Итерация {i+1}, a = {a}, b = {b}, epsilon_n = {(b-a)/2}, x1 = {round(x1, 5)}, x2 = {round( x2, 5)}, f(x1) = {round(calculate_question(x1),5)}, f(x2) = {round(calculate_question(x2),5)}, f(x1) > f(x2)")
            
        if ((b-a)/2 > epsilon):
            continue
        else:
            break
    x = (a+b)/2
    print(f"{quation_name} принимает минимум при x = {round(x,5)}, f(x) = {round(calculate_question(x),5)}")
    
def golden_ratio(a,b, epsilon):
    x1 = a + (3 - math.sqrt(5)) / 2 * (b - a)
    x2 = a + (math.sqrt(5) - 1) / 2 * (b - a)
    t = (math.sqrt(5)-1)/2
    epsilon_n = (b-a)/2
    for i in range(25):
        if(epsilon_n > epsilon):
            if calculate_question(x1) <= calculate_question(x2):
                b = x2
                x2 = x1
                x1 =b - t*(b-a)
                print(f"Итерация {i+1}, a = {a}, b = {b}, epsilon_n = {epsilon_n}, x1 = {round(x1,5)}, x2 = {round(x2,5)}, f(x1) = {round(calculate_question(x1),5)}, f(x2) = {round(calculate_question(x2),5)}, f(x1) <= f(x2)")
            else:
                a=x1
                x1 = x2
                x2 = a + t*(b-a)
                print(f"Итерация {i+1}, a = {a}, b = {b}, epsilon_n = {epsilon_n}, x1 = {round(x1,5)}, x2 = {round(x2,5)}, f(x1) = {round(calculate_question(x1),5)}, f(x2) = {round(calculate_question(x2),5)}, f(x1) > f(x2)")
            epsilon_n *= t
        else:
            break
    x = (a+b)/2
    print(f"{quation_name} принимает минимум при x = {round(x,5)}, f(x) = {round(calculate_question(x),5)}")
    
def newton_method(a,b, epsilon):
    x = (a+b)/2
    for i in range(25):
        if abs(df_dx(x)) > epsilon:
            x = x - df_dx(x)/df2_dx2(x)
            print(f"Итерация {i+1}, a = {a}, b = {b}, x = {round(x,5)}, f(x) = {round(calculate_question(x),5)}, f'(x) = {round(df_dx(x),5)}, |{round(df_dx(x),5)}| <= {epsilon}")
        else:
            break
    print(f"{quation_name} принимает минимум при x = {round(x,5)}, f(x) = {round(calculate_question(x),5)}")
    
print("\n Метод половинного деления:")
half_hord(a,b, epsilon)

print("\n Метод золотого сечения:")
golden_ratio(a,b, epsilon)

print("\n Метод Ньёмана:")
newton_method(a,b, epsilon)