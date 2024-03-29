import math
import numpy as np
import matplotlib.pyplot as plt

a = float(1)
b = float(1.5)
epsilon = float(pow(10, -10))
quation_name = "x^2 - 2x + e^(-x)"


def calculate_question(x):
    return x * x - 2 * x + math.exp(-x)


def df_dx(x):
    return 2 * x - 2 - math.exp(-x)


def df2_dx2(x):
    return 2 + math.exp(-x)


def half_division(a, b, epsilon):

    for i in range(25):
        x1 = (b + a - epsilon) / 2
        x2 = (b + a + epsilon) / 2

        if calculate_question(x1) <= calculate_question(x2):
            b = x2
            print(
                f"Итерация {i+1}, a = {a}, b = {b}"
            )
        else:
            a = x1
            print(
                f"Итерация {i+1}, a = {a}, b = {b}"
            )

        if (b - a) / 2 > epsilon:
            continue
        else:
            break
    x = (a + b) / 2
    print(
        f"{quation_name} принимает минимум при x = {x}, f(x) = {calculate_question(x)}"
    )


def golden_ratio(a, b, epsilon):
    x1 = a + (3 - math.sqrt(5)) / 2 * (b - a)
    x2 = a + (math.sqrt(5) - 1) / 2 * (b - a)
    t = (math.sqrt(5) - 1) / 2
    epsilon_n = (b - a) / 2
    for i in range(25):
        if epsilon_n > epsilon:
            if calculate_question(x1) <= calculate_question(x2):
                b = x2
                x2 = x1
                x1 = b - t * (b - a)
                print(
                    f"Итерация {i+1}, a = {a}, b = {b}"
                )
            else:
                a = x1
                x1 = x2
                x2 = a + t * (b - a)
                print(
                    f"Итерация {i+1}, a = {a}, b = {b}"
                )
            epsilon_n *= t
        else:
            break
    x = (a + b) / 2
    print(
        f"{quation_name}  принимает минимум при x = {x}, f(x) = {calculate_question(x)}"
    )


def newton_method(a, b, epsilon):
    x = (a + b) / 2
    for i in range(25):
        if abs(df_dx(x)) > epsilon:
            x = x - df_dx(x) / df2_dx2(x)
            print(
                f"Итерация {i+1}, x{i+1} ={x} f'(x{i+1}) = {str('%.2e' % df_dx(x))}"
            )
        else:
            break
    print(
        f"{quation_name}  принимает минимум при x = {x}, f(x) = {str('%.2e' % calculate_question(x))}"
    )


print("\n Метод половинного деления:")
half_division(a, b, epsilon)

print("\n Метод золотого сечения:")
golden_ratio(a, b, epsilon)

print("\n Метод Ньютона:")
newton_method(a, b, epsilon)

x_values = np.linspace(0.5, 2, 400)


def func(x):
    return x**2 - 2 * x + np.exp(-x)


y_values = func(x_values)


plt.plot(x_values, y_values, label="$f(x) = x^2 - 2x + e^{-x}$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("График функции $f(x) = x^2 - 2x + e^{-x}$")
plt.axhline(0, color="red", linewidth=0.5)
plt.legend()
plt.grid(True)
plt.show()
