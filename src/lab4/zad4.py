import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
import scipy.interpolate as interpolate
from labb4.zad1 import to_table


def compare_results(min, max, points_number, function1, function2, function_name):
    table = []
    step = (max - min) / points_number
    for i in np.arange(min + (step / 2), max + (step / 2), step):
        table.append([i, function1(i), function2(i), abs(function2(i) - function1(i)) / abs(function1(i)),])
    print(tabulate(table,
                   headers=['x', function_name, 'interpolated ' + function_name, 'relative error'],
                   tablefmt="fancy_grid", floatfmt=".10f"))


def to_chart(min, max, points_number, function1, function2, function_name):
    x_axis = np.linspace(min, max, points_number)
    f1_values = function1(x_axis)
    f2_values = function2(x_axis)

    plt.plot(x_axis, f1_values, label=function_name)
    plt.plot(x_axis, f2_values, label="Interpolation B-spline " + function_name)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(function_name)
    plt.legend()
    plt.show()


def calculate_b_spline(x_values, y_values):
    t, c, k = interpolate.splrep(x_values, y_values, s=0, k=2)
    return interpolate.BSpline(t, c, k, extrapolate=False)


def n_nodes_interpolation(min, max, n):
    x_sqrt, y_sqrt = to_table(min, max, n,np.sqrt)
    x_sin, y_sin = to_table(min, max, n, np.sin)
    f = lambda x: x ** 3 + 2 * x
    x_f, y_f = to_table(min, max, n, f)

    compare_results(min, max, n, np.sqrt, calculate_b_spline(x_sqrt, y_sqrt), "sqrt(x)")
    compare_results(min, max, n, np.sin, calculate_b_spline(x_sin, y_sin), "sin(x)")
    compare_results(min, max, n, f, calculate_b_spline(x_f, y_f), "x^3 + 2*x")

    to_chart(min, max, 8000, np.sqrt, calculate_b_spline(x_sqrt, y_sqrt), "sqrt(x)")
    to_chart(min, max, 8000, np.sin, calculate_b_spline(x_sin, y_sin), "sin(x)")
    to_chart(min, max, 8000, f, calculate_b_spline(x_f, y_f), "x^3 + 2*x")


n_nodes_interpolation(0, 10, 30)


