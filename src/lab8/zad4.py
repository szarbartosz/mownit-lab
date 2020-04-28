from scipy import optimize
from tabulate import tabulate
from lab8.zad1 import bisection_method
from lab8.zad2 import newton_raphson_method
from lab8.zad3 import secant_euler_method


def compare(func, a, b, n, func_name):
    scipy_bisect = optimize.bisect(func, a, b)  # used as reference value
    c_bis, E = bisection_method(func, a, b, n)
    if c_bis is None:
      c = "None"
    c_new = newton_raphson_method(func, a, b, n)
    if c_new is None:
      c = "None"
    c_eul = secant_euler_method(func, a, b, n)
    if c_eul is None:
      c = "None"

    print(f"f(x): {func_name}, interval: ({a}, {b})")
    table = [["scipy method", scipy_bisect, 0],
           ["bisection method", c_bis, (abs(c_bis - scipy_bisect) / abs(scipy_bisect))],
           ["newton-Raphson method", c_new, (abs(c_new - scipy_bisect) / abs(scipy_bisect))],
           ["secant method", c_eul, (abs(c_eul - scipy_bisect) / abs(scipy_bisect))]]

    print(tabulate(table, headers=["method", "root", "error"], tablefmt="fancy_grid"))