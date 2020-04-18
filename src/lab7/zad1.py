import numpy as np
from tabulate import tabulate
import scipy.integrate as integrate
from scipy.special.orthogonal import roots_legendre
from lab6.zad1 import rectangle_method, trapeze_method, simpson_method


def gauss_legendre_method(func, a, b, deg):
    [x, w] = roots_legendre(deg + 1)
    A = 0.5 * (b - a)
    B = 0.5 * (b - a) * x + 0.5 * (b + a)
    result = A * sum(w * np.vectorize(func)(B))
    return result


def calculate_integral(func, a, b, intervals, func_name):
    rectangle_integral = rectangle_method(func, a, b, intervals)
    trapeze_integral = trapeze_method(func, a, b, intervals)
    simpson_integral = simpson_method(func, a, b, intervals)
    gauss_legendre_integral_2 = gauss_legendre_method(func, a, b, 2)
    gauss_legendre_integral_3 = gauss_legendre_method(func, a, b, 3)
    gauss_legendre_integral_4 = gauss_legendre_method(func, a, b, 4)
    gauss_legendre_integral_5 = gauss_legendre_method(func, a, b, 5)
    numpy_integral = integrate.quad(func, a, b)[0]
    table = [
        ["rectangle", rectangle_integral, abs(rectangle_integral - numpy_integral) / abs(numpy_integral)],
        ["trapeze", trapeze_integral, abs(trapeze_integral - numpy_integral) / abs(numpy_integral)],
        ["simpson", simpson_integral, abs(simpson_integral - numpy_integral) / abs(numpy_integral)],
        ["gauss, deg = 2", gauss_legendre_integral_2, abs(gauss_legendre_integral_2 - numpy_integral) / abs(numpy_integral)],
        ["gauss, deg = 3", gauss_legendre_integral_3, abs(gauss_legendre_integral_3 - numpy_integral) / abs(numpy_integral)],
        ["gauss, deg = 4", gauss_legendre_integral_4, abs(gauss_legendre_integral_4 - numpy_integral) / abs(numpy_integral)],
        ["gauss, deg = 5", gauss_legendre_integral_5, abs(gauss_legendre_integral_5 - numpy_integral) / abs(numpy_integral)],
        ["numpy", numpy_integral, 0.0]
    ]
    print(tabulate(table, headers=['method', 'value', 'error [%]'], tablefmt="fancy_grid", floatfmt=".10f"))

f1 = lambda x: 3 * x**3 - 1
f2 = lambda x: 2 * x**2
f3 = lambda x: 4 * np.math.sin(x)

# calculate_integral(f1, -3, 10, 100, '3 * x^3 - 1')
# calculate_integral(f2, -20, 12, 100, '2 * x**2')
# calculate_integral(f3, -3, 10, 100, '4 * sin(x)')