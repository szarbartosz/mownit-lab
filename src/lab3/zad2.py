import math
import sympy as sp
from tabulate import tabulate
from lab3.zad1 import to_table


def lagrange_interpolation(x_values, y_values):
    if len(x_values) != len(y_values):
        print("number of x and y values must be equal")
        return -1
    x = sp.symbols('x')
    y = 0
    for k in range(len(x_values)):
        i = 1
        for j in range(len(x_values)):
            if j != k:
                i *= ((x - x_values[j]) / (x_values[k] - x_values[j]))
        y += i * y_values[k]
    return sp.simplify(y)

result = []

x_arr, y_arr = to_table(0, 10, 3, math.sqrt)
result.append(['sqrt(x)', lagrange_interpolation(x_arr, y_arr)])

x_arr, y_arr = to_table(0, 10, 3, math.sin)
result.append(['sin(x)', lagrange_interpolation(x_arr, y_arr)])

f = lambda x: x ** 3 + 2 * x
x_arr, y_arr = to_table(0, 10, 3, f)
result.append(["x^3 + 2x", lagrange_interpolation(x_arr, y_arr)])


print(tabulate(result, headers=['function', 'Lagrange interpolation polynomial'], tablefmt="fancy_grid", floatfmt=".10f"))