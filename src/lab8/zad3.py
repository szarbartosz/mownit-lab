from tabulate import tabulate
from lab8.zad1 import draw_plot


def secant_euler_method(func, x0, x1, n):
    if func(x0) * func(x1) >= 0 or n <= 0 or x0 >= x1:
        return None
    for i in range(n):
        x2 = x1 - (func(x1) * (x1 - x0)) / (func(x1) - func(x0))
        x0, x1 = x1, x2
    return x2


def secant_euler_calculate(func, a, b, n, func_name):
    c = secant_euler_method(func, a, b, n)
    if c is None:
        c = "None"
    table = [
        [func_name, f"({a}, {b})", n, c]
    ]
    print(tabulate(table, headers=['f(x)', 'interval', 'iterations', 'root'], tablefmt="fancy_grid"))
    draw_plot(func, a, b, n, func_name)