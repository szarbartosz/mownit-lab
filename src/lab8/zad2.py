import scipy.misc as misc
from tabulate import tabulate
from lab8.zad1 import draw_plot


def newton_raphson_method(func, a, b, n):
    if func(a) * func(b) >= 0 or n < 1 or a >= b:
      return None
    x = b
    for i in range(n):
        if misc.derivative(func, x) == 0:
            return None
        h = func(x) / misc.derivative(func, x)
        x = x - h
    return x


def newton_rapson_calculate(func, a, b, n, func_name):
    c = newton_raphson_method(func, a, b, n)
    if c is None:
        c = "None"
    table = [
        [func_name, f"({a}, {b})", n, c]
    ]
    print(tabulate(table, headers=['f(x)', 'interval', 'iterations', 'root'], tablefmt="fancy_grid"))
    draw_plot(func, a, b, n, func_name)