import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
import math
from lab3.zad1 import to_table


def lagrange_interpolation(x_values, y_values, x):
    if len(x_values) != len(y_values):
        print("number of x and y values must be equal")
        return -1
    y = 0
    for k in range(len(x_values)):
        i = 1
        for j in range(len(x_values)):
            if j != k:
                i = i * ((x - x_values[j]) / (x_values[k] - x_values[j]))
        y += i * y_values[k]
    return sp.simplify(y)


def compare_results(min, max, points_number, function1, function2, function_name):
    table = []
    step = (max - min) / points_number
    for i in np.arange(min + (step / 2), max + (step / 2), step):
        table.append([i, function1(i), function2(i), abs(function2(i) - function1(i)) / abs(function1(i)), abs(function1(i) - function2(i))])
    print(tabulate(table, headers=['x', function_name, 'interpolated ' + function_name, 'relative error', 'absolute error'],
                   tablefmt="fancy_grid", floatfmt=".10f"))


def to_chart(min, max, points_number, function1, function2, function_name):
    x_axis = []
    function1_values = []
    function2_values = []
    step = (max - min) / points_number
    for i in np.arange(min, max + step, step):
        x_axis.append(i)
        function1_values.append(function1(i))
        function2_values.append(function2(i))
    plt.plot(x_axis, function1_values, label=function_name)
    plt.plot(x_axis, function2_values, label="interpolated " + function_name)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(function_name)
    plt.legend()
    plt.show()


x_sqrt, y_sqrt = to_table(0, 10, 4, math.sqrt, "sqrt")
x_sin, y_sin = to_table(0, 10, 4, math.sin, "sin")
f = lambda x: x ** 3 + 2 * x
x_f, y_f = to_table(0, 10, 4, f, "x^3 + 2x")

sqrt_interpolation = lambda x: lagrange_interpolation(x_sqrt, y_sqrt, x)
sin_interpolation = lambda x: lagrange_interpolation(x_sin, y_sin, x)
f_interpolation = lambda x: lagrange_interpolation(x_f, y_f, x)

compare_results(0, 10, 4, math.sqrt, sqrt_interpolation, "sqrt(x)")
compare_results(0, 10, 4, math.sin, sin_interpolation, "sin(x)")
compare_results(0, 10, 4, f, f_interpolation, "x^3 + 2*x")

to_chart(0, 10, 80000, math.sqrt, sqrt_interpolation, "sqrt(x)")
to_chart(0, 10, 80000, math.sin, sin_interpolation, "sin(x)")
to_chart(0, 10, 80000, f, f_interpolation, "x^3 + 2*x")
