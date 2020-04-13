import numpy as np
from tabulate import tabulate
import scipy.integrate as integrate
import matplotlib.pyplot as plt
from lab6.zad1 import rectangle_method, trapeze_method, simpson_method

f1 = lambda x: x
f2 = lambda x: 2 * x ** 2
f3 = lambda x: 4 * np.math.sin(x)
f4 = lambda x: np.exp(x)
f5 = lambda x: x * np.math.sin(x) ** 2 + 2 * np.math.cos(x)
f6 = lambda x: np.math.cos((x + 1) / (x ** 2 + 0.04)) * np.exp(x)


def draw_plot(func, a, b, intervals, func_name):
    t = np.linspace(a, b, intervals)
    plt.plot(t, np.vectorize(func)(t), label=func_name)
    plt.title(func_name)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()


def calculate_integral(func, a, b, intervals, func_name):
    draw_plot(func, a, b, intervals, func_name)
    rectangle_integral = rectangle_method(func, a, b, intervals)
    trapeze_integral = trapeze_method(func, a, b, intervals)
    simpson_integral = simpson_method(func, a, b, intervals)
    numpy_integral = integrate.quad(func, a, b)[0]
    table = [
        ["rectangle", rectangle_integral, abs(rectangle_integral - numpy_integral) / abs(numpy_integral)],
        ["trapeze", trapeze_integral, abs(trapeze_integral - numpy_integral) / abs(numpy_integral)],
        ["simpson", simpson_integral, abs(simpson_integral - numpy_integral) / abs(numpy_integral)],
        ["numpy", numpy_integral, 0.0]
    ]
    print(tabulate(table, headers=['method', 'value', 'error [%]'], tablefmt="fancy_grid", floatfmt=".10f"))


calculate_integral(f1, 69, 420, 2137, 'x')
calculate_integral(f2, 69, 420, 2137, '2*x^2')
calculate_integral(f3, 69, 420, 2137, '4*sin(x)')
calculate_integral(f4, 69, 420, 2137, 'e^x')
calculate_integral(f5, 69, 420, 2137, 'x*sin^2(x)+2*cos(x)')
calculate_integral(f6, 69, 420, 2137, 'cos((x+1) / (x^2+0.04)) * e^x')