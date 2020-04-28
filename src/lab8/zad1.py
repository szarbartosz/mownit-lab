import math
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

f1 = lambda x: 2 * x ** 2 - 2 * x + 1
f2 = lambda x: -26 + 85 * x - 91 * x ** 2 + 44 * x ** 3 - 8 * x ** 4 + x ** 5
f3 = lambda x: 4 ** x - 3 ** (2 * x) + 2 ** (3 * x) - 1
f4 = lambda x: 3 * x + math.sin(x) - math.cos(x) ** 3
f5 = lambda x: 27 * x ** 3 - 3 * x + 1


def draw_plot(func, a, b, n, func_name):
    domain = np.linspace(a, b, n)
    plt.plot(domain, np.vectorize(func)(domain), label=func_name)
    plt.title(func_name)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()


def bisection_method(func, a, b, n):
    if func(a) * func(b) >= 0 or n <= 0 or a >= b:
        return None, None
    else:
        d = b - a
        c = 1
        for i in range(n):
            c = (a + b) / 2
            if func(c) == 0:
                return c, d / 2 ** i
            elif func(c) * func(a) < 0:
                b = c
            else:
                a = c

        E = d / 2 ** n
        return c, E


def bisection_calculate(func, a, b, n, func_name):
    c, E = bisection_method(func, a, b, n)
    if c is None:
      c = "None"
    if E is None:
      E = "None"

    table = [
        [func_name, f"({a}, {b})", n, c, E]
    ]
    print(tabulate(table, headers=['f(x)', 'interval', 'iterations', 'root', 'error'], tablefmt="fancy_grid"))
    draw_plot(func, a, b, n, func_name)