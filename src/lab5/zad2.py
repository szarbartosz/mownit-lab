import math
import numpy as np
import matplotlib.pyplot as plt
from labb5.zad1 import to_table

def compare_charts(x_values, y_values, x_data, y_data, function_name):
    params = {'legend.fontsize': 'x-large',
                  'axes.labelsize': 'x-large',
                  'axes.titlesize': 'x-large',
                  'xtick.labelsize': 'x-large',
                  'ytick.labelsize': 'x-large'}
    plt.rcParams.update(params)
    plt.plot(x_values, y_values, label="approx of "+ function_name)
    plt.plot(x_data, y_data, 'or', label="actual values of " + function_name)
    plt.grid(True, which='both')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.xticks(rotation=90)
    plt.legend()
    plt.show()

def python_approx(min, max, n, degree):

    x_sqrt, y_sqrt = to_table(min, max, n, math.sqrt)
    x_sin, y_sin = to_table(min, max, n, math.sin)
    f = lambda x: x ** 3 + 2 * x
    x_f, y_f = to_table(min, max, n, f)

    for i in range(1, degree + 1):

        sqrt_polynomial = np.polyfit(x_sqrt, y_sqrt, deg=i, full=True)
        sin_polynomial = np.polyfit(x_sin, y_sin, deg=i, full=True)
        f_polynomial = np.polyfit(x_f, y_f, deg=i, full=True)

        sqrt_eval = np.polyval(sqrt_polynomial[0], x_sqrt)
        sin_eval = np.polyval(sin_polynomial[0], x_sin)
        f_eval = np.polyval(f_polynomial[0], x_f)

        compare_charts(x_sqrt, sqrt_eval, x_sqrt, y_sqrt, "sqrt(x)")
        compare_charts(x_sin, sin_eval, x_sin, y_sin, "sin(x)")
        compare_charts(x_f, f_eval, x_f, y_f, "x^3 + 2*x")

# python_approx(0, 10, 100, 10)


cases = [1,1,1,1,3,3,4,6,7,11,14,17,20,20,20,33,25,25,25,26,26,26,28,29,33,41,53,59,65,73,85,93,105,132,144,157,164,186,210,230,239,254,268,284,317,349,408,455,488,514,568,620,675,716,780,814,829,829,873,950,996,1046,1089,1128,1193,1291,1387]
dates = ['1/21/2020','1/22/2020','1/23/2020','1/24/2020','1/25/2020','1/26/2020','1/27/2020','1/28/2020','1/29/2020','1/30/2020','1/31/2020','2/1/2020','2/2/2020','2/3/2020','2/4/2020','2/5/2020','2/6/2020','2/7/2020','2/8/2020','2/9/2020','2/10/2020','2/11/2020','2/12/2020','2/13/2020','2/14/2020','2/15/2020','2/16/2020','2/17/2020','2/18/2020','2/19/2020','2/20/2020','2/21/2020','2/22/2020','2/23/2020','2/24/2020','2/25/2020','2/26/2020','2/27/2020','2/28/2020','2/29/2020','3/1/2020','3/2/2020','3/3/2020','3/4/2020','3/5/2020','3/6/2020','3/7/2020','3/8/2020','3/9/2020','3/10/2020','3/11/2020','3/12/2020','3/13/2020','3/14/2020','3/15/2020','3/16/2020','3/17/2020','3/18/2020','3/19/2020','3/20/2020','3/21/2020','3/22/2020','3/23/2020','3/24/2020','3/25/2020','3/26/2020','3/27/2020']

def coronavirus_approx_python(dates, cases, degree):
    for i in range(1, degree + 1):
        cases_polynomial = np.polyfit(np.linspace(1, len(dates), len(dates)), cases, degree)
        cases_values = np.polyval(cases_polynomial, np.linspace(1, len(dates), len(dates)))

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

# coronavirus_approx_python(dates, cases, 8)