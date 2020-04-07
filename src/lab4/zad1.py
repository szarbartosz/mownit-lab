import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
import math


def calculate_coef(x_values, y_values):
    n = len(x_values)
    arr = np.copy(y_values)
    for i in range(1, n):
        for j in range(n - 1, i - 1, -1):
            arr[j] = float(arr[j] - arr[j - 1]) / float(x_values[j] - x_values[j - i])
    return arr


def newton_interpolation(coefficients_array, x_values, x):
    n = len(coefficients_array)
    y = 0
    for k in range(n):
        i = 1
        for j in range(k):
            i *= (x - x_values[j])
        y += i * coefficients_array[k]
    return y


def to_table(min, max, points_number, function):
    table = []
    x_values = []
    y_values = []
    step = (max - min) / points_number
    for i in np.arange(min, max + step, step):
        table.append([i, function(i)])
        x_values.append(i)
        y_values.append(function(i))
    return x_values, y_values


def compare_results(min, max, points_number, function1, function2, function_name):
    table = []
    step = (max - min) / points_number
    for i in np.arange(min + (step / 2), max + (step / 2), step):
        table.append([i, function1(i), function2(i), abs(function2(i) - function1(i)) / abs(function1(i)),
                      abs(function1(i) - function2(i))])
    print(tabulate(table,
                   headers=['x', function_name, 'interpolated ' + function_name, 'relative error', 'absolute error'],
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


def n_nodes_interpolation(min, max, n):
    x_sqrt, y_sqrt = to_table(min, max, n, math.sqrt)
    x_sin, y_sin = to_table(min, max, n, math.sin)
    f = lambda x: x ** 3 + 2 * x
    x_f, y_f = to_table(min, max, n, f)

    coef_sqrt = calculate_coef(x_sqrt, y_sqrt)
    coef_sin = calculate_coef(x_sin, y_sin)
    coef_f = calculate_coef(x_f, y_f)

    sqrt_interpolation = lambda x: newton_interpolation(coef_sqrt, x_sqrt, x)
    sin_interpolation = lambda x: newton_interpolation(coef_sin, x_sin, x)
    f_interpolation = lambda x: newton_interpolation(coef_f, x_f, x)

    compare_results(min, max, n, math.sqrt, sqrt_interpolation, "sqrt(x)")
    compare_results(min, max, n, math.sin, sin_interpolation, "sin(x)")
    compare_results(min, max, n, f, f_interpolation, "x^3 + 2*x")

    to_chart(min, max, 80000, math.sqrt, sqrt_interpolation, "sqrt(x)")
    to_chart(min, max, 80000, math.sin, sin_interpolation, "sin(x)")
    to_chart(min, max, 80000, f, f_interpolation, "x^3 + 2*x")


n_nodes_interpolation(0, 10, 3)
n_nodes_interpolation(0, 10, 5)
n_nodes_interpolation(0, 10, 8)
