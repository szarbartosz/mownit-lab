import math
import numpy as np
from tabulate import tabulate


def to_table(min, max, points_number, function, function_name):
    table = []
    x_values = []
    y_values = []
    step = (max - min) / points_number
    for i in np.arange(min, max + step, step):
        table.append([i, function(i)])
        x_values.append(i)
        y_values.append(function(i))
    print(tabulate(table, headers=["x", function_name], tablefmt="fancy_grid", floatfmt=".10f"))
    return x_values, y_values


to_table(0, 10, 3, math.sqrt, "sqrt(x)")
to_table(0, 10, 3, math.sin, "sin(x)")
f = lambda x: x ** 3 + 2 * x
to_table(0, 10, 3, f, "x^3+2x")