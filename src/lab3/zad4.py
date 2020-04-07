import math
from labb3.zad1 import to_table
from labb3.zad3 import lagrange_interpolation, compare_results, to_chart


def n_nodes_interpolation(min, max, n):
    x_sqrt, y_sqrt = to_table(0, 10, n, math.sqrt)
    x_sin, y_sin = to_table(0, 10, n, math.sin)
    f = lambda x: x ** 3 + 2 * x
    x_f, y_f = to_table(0, 10, n, f)

    sqrt_interpolation = lambda x: lagrange_interpolation(x_sqrt, y_sqrt, x)
    sin_interpolation = lambda x: lagrange_interpolation(x_sin, y_sin, x)
    f_interpolation = lambda x: lagrange_interpolation(x_f, y_f, x)

    compare_results(0, 10, 4, math.sqrt, sqrt_interpolation, "sqrt(x)")
    compare_results(0, 10, 4, math.sin, sin_interpolation, "sin(x)")
    compare_results(0, 10, 4, f, f_interpolation, "x^3 + 2*x")

    to_chart(0, 10, 80000, math.sqrt, sqrt_interpolation, "sqrt(x)")
    to_chart(0, 10, 80000, math.sin, sin_interpolation, "sin(x)")
    to_chart(0, 10, 80000, f, f_interpolation, "x^3 + 2*x")