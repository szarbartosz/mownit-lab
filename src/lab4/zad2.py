import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
import math
from labb4.zad1 import to_table

def hermite_interpolation_polynomial(x_values, y_values):
    n = len(x_values)
    derivatives = [0] * n
    if n != len(y_values):
        print("error")
        exit(1)

    for i in range(1, n):
        if x_values[i] == x_values[i - 1]:
            derivatives[i] = derivatives[i - 1] + 1
        else:
            derivatives[i] = 0

    for i in range(1, n):
        for j in range(n - 1, i - 1, -1):
            if derivatives[j] == 0:
                y_values[j] = (y_values[j] - y_values[int(j - 1 - derivatives[j - 1])]) / (
                            x_values[j] - x_values[j - i]);
            else:
                y_values[j] /= float(i)
                derivatives[j] -= 1

    for j in range(n - 1, -1, -1):
        for i in range(j, n - 1, 1):
            y_values[i] = y_values[i] - y_values[i + 1] * x_values[j]

    polynomial = 0
    X = sp.symbols('x')
    for i in range(n):
        polynomial += y_values[i] * pow(X, i)
    return polynomial


def eval(f, x):
    X = sp.symbols('x')
    return f.evalf(subs={X: x})


def compare_results(min, max, points_number, function1, function2, polynomial, function_name):
    table = []
    step = (max - min) / points_number
    for i in np.arange(min + (step / 2), max + (step / 2), step):
        table.append([i, function1(i), function2(polynomial, i), abs(function2(polynomial, i) - function1(i)) / abs(function1(i)),])
    print(tabulate(table,
                   headers=['x', function_name, 'interpolated ' + function_name, 'relative error'],
                   tablefmt="fancy_grid", floatfmt=".10f"))


def to_chart(min, max, points_number, function1, function2, polynomial, function_name):
    x_axis = []
    function1_values = []
    function2_values = []
    step = (max - min) / points_number
    for i in np.arange(min, max + step, step):
        x_axis.append(i)
        function1_values.append(function1(i))
        function2_values.append(function2(polynomial, i))
    plt.plot(x_axis, function1_values, label=function_name)
    plt.plot(x_axis, function2_values, label="interpolated " + function_name)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(function_name)
    plt.legend()
    plt.show()


def n_nodes_interpolation(min, max, n):
    x_sqrt, y_sqrt = to_table(min, max, n, math.sqrt)
    x_sin, y_sin = to_table(min, max, n, math.sin)
    f = lambda x: x ** 3 + 2 * x
    x_f, y_f = to_table(min, max, n, f)

    sqrt_interpolation = hermite_interpolation_polynomial(x_sqrt, y_sqrt)
    sin_interpolation = hermite_interpolation_polynomial(x_sin, y_sin)
    f_interpolation = hermite_interpolation_polynomial(x_f, y_f)

    compare_results(min, max, n, math.sqrt, eval, sqrt_interpolation, "sqrt(x)")
    compare_results(min, max, n, math.sin, eval, sin_interpolation, "sin(x)")
    compare_results(min, max, n, f, eval, f_interpolation, "x^3 + 2*x")

    to_chart(min, max, 80000, math.sqrt, eval, sqrt_interpolation, "sqrt(x)")
    to_chart(min, max, 80000, math.sin, eval, sin_interpolation, "sin(x)")
    to_chart(min, max, 80000, f, eval, f_interpolation, "x^3 + 2*x")


n_nodes_interpolation(0, 10, 3)
n_nodes_interpolation(0, 10, 5)
n_nodes_interpolation(0, 10, 8)

