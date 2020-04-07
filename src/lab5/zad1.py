from tabulate import tabulate
import sympy as sp
import matplotlib.pyplot as plt
import math
import numpy as np

def to_table(min, max, points_number, function):
    table = []
    x_values = []
    y_values = []
    step = (max - min) / points_number
    for i in np.arange(min, max + step, step):
        table.append([i, function(i)])
        x_values.append(i)
        y_values.append(function(i))
    return x_values, y_values


def square_approx_polynomial(x_values, y_values, degree):
    n = len(x_values)

    values = [0] * (2 * degree + 1)
    for i in range(2 * degree + 1):
        for j in range(n):
            values[i] += pow(x_values[j], i)

    B_arr = np.zeros(degree + 1)
    for i in range(degree + 1):
        for j in range(n):
            B_arr[i] += (pow(x_values[j], i) * y_values[j])

    C_mat = np.zeros((degree + 1, degree + 1))
    for i in range(degree + 1):
        for j in range(degree + 1):
            C_mat[i][j] = values[i + j]

    A = np.linalg.solve(C_mat, B_arr)

    polynomial = 0
    X = sp.symbols('x')
    for i in range(degree + 1):
        polynomial += pow(X, i) * A[i]

    return sp.simplify(polynomial)


def eval(f, x):
    X = sp.symbols('x')
    return f.evalf(subs={X: x})


def to_chart(min, max, points_number, function1, function2, function_name):
    x_axis = []
    function1_values = []
    function2_values = []
    step = (max - min) / points_number
    for i in np.arange(min, max + step, step):
        x_axis.append(i)
        function1_values.append(function1(i))
        function2_values.append(function2(i))
    plt.plot(x_axis, function1_values, label=function_name)
    plt.plot(x_axis, function2_values, label="approximation of " + function_name)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(function_name)
    plt.legend()
    plt.show()


def compare_results(min, max, points_number, function1, function2, function_name, error_arr, show_table):
    table = []
    step = (max - min) / points_number
    for i in np.arange(min + (step / 2), max + (step / 2), step):
        table.append([i, function1(i), function2(i), abs(function2(i) - function1(i)) / abs(function1(i))])
        error_arr.append(abs(function2(i) - function1(i)) / abs(function1(i)))
    if show_table:
        print(tabulate(table,
                       headers=['x', function_name, 'interpolated ' + function_name, 'relative error'],
                       tablefmt="fancy_grid", floatfmt=".10f"))


def square_approx_n_degree(min, max, n, degree, show_table):
    x_sqrt, y_sqrt = to_table(min, max, n, math.sqrt)
    x_sin, y_sin = to_table(min, max, n, math.sin)
    f = lambda x: x ** 3 + 2 * x
    x_f, y_f = to_table(min, max, n, f)

    for i in range(1, degree + 1):
        sqrt_polynomial = square_approx_polynomial(x_sqrt, y_sqrt, i)
        sin_polynomial = square_approx_polynomial(x_sin, y_sin, i)
        f_polynomial = square_approx_polynomial(x_f, y_f, i)

        sqrt_eval = lambda x: eval(sqrt_polynomial, x)
        sin_eval = lambda x: eval(sin_polynomial, x)
        f_eval = lambda x: eval(f_polynomial, x)

        error_arr = []
        to_chart(min, max, 100, math.sqrt, sqrt_eval, "sqrt(x)")
        compare_results(min, max, n, math.sqrt, sqrt_eval, "sqrt(x)", error_arr, show_table)
        print("relative error for sqrt - approx of {} degree: {} %".format(i, (np.sum(error_arr) / len(error_arr))))

        error_arr = []
        to_chart(min, max, 100, math.sin, sin_eval, "sin(x)")
        compare_results(min, max, n, math.sin, sin_eval, "sqrt(x)", error_arr, show_table)
        print("relative error for sin - approx of {} degree: {} %".format(i, (np.sum(error_arr) / len(error_arr))))

        error_arr = []
        to_chart(min, max, 100, f, f_eval, "x^3 + 2*x")
        compare_results(min, max, n, f, f_eval, "sqrt(x)", error_arr, show_table)
        print("relative error for x^3 + 2*x - approx of {} degree: {} %".format(i, (np.sum(error_arr) / len(error_arr))))


# square_approx_n_degree(0, 10, 3, 10, False)
# square_approx_n_degree(0, 10, 4, 10, False)
# square_approx_n_degree(0, 10, 5, 10, False)
# square_approx_n_degree(0, 10, 8, 10, False)

def calculate_values(polynomial, scope):
  values = []
  for number in scope:
    values.append(eval(polynomial, number))
  return values

cases = [1,1,1,1,3,3,4,6,7,11,14,17,20,20,20,33,25,25,25,26,26,26,28,29,33,41,53,59,65,73,85,93,105,132,144,157,164,186,210,230,239,254,268,284,317,349,408,455,488,514,568,620,675,716,780,814,829,829,873,950,996,1046,1089,1128,1193,1291,1387]
dates = ['1/21/2020','1/22/2020','1/23/2020','1/24/2020','1/25/2020','1/26/2020','1/27/2020','1/28/2020','1/29/2020','1/30/2020','1/31/2020','2/1/2020','2/2/2020','2/3/2020','2/4/2020','2/5/2020','2/6/2020','2/7/2020','2/8/2020','2/9/2020','2/10/2020','2/11/2020','2/12/2020','2/13/2020','2/14/2020','2/15/2020','2/16/2020','2/17/2020','2/18/2020','2/19/2020','2/20/2020','2/21/2020','2/22/2020','2/23/2020','2/24/2020','2/25/2020','2/26/2020','2/27/2020','2/28/2020','2/29/2020','3/1/2020','3/2/2020','3/3/2020','3/4/2020','3/5/2020','3/6/2020','3/7/2020','3/8/2020','3/9/2020','3/10/2020','3/11/2020','3/12/2020','3/13/2020','3/14/2020','3/15/2020','3/16/2020','3/17/2020','3/18/2020','3/19/2020','3/20/2020','3/21/2020','3/22/2020','3/23/2020','3/24/2020','3/25/2020','3/26/2020','3/27/2020']


def coronavirus_approx(dates, cases, degree):
    for i in range(1, degree + 1):
        cases_polynomial = square_approx_polynomial(np.linspace(1, len(cases), len(cases)), cases, i)
        cases_values = calculate_values(cases_polynomial, np.linspace(1, len(cases), len(cases)))

        params = {'legend.fontsize': 'x-large',
                  'figure.figsize': (20, 12),
                  'axes.labelsize': 'x-large',
                  'axes.titlesize': 'x-large',
                  'xtick.labelsize': 'x-large',
                  'ytick.labelsize': 'x-large'}
        plt.rcParams.update(params)
        plt.title(f'approx of degree {i}')
        plt.plot(dates, cases_values, label="approximated number of cases in Japan")
        plt.plot(dates, cases, 'ro', label="actual data")
        plt.grid(True, which='both')
        plt.xlabel('x-axis')
        plt.ylabel('y-axis')
        plt.xticks(rotation=90)
        plt.legend()
        plt.show()

# coronavirus_approx(dates, cases, 8)