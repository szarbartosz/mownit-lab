import numpy as np
from scipy.linalg import norm

def chebyshev(A, b, max_iterations, l_max, l_min, eps, n=10):
    d = (l_max + l_min) / 2
    c = (l_max - l_min) / 2
    x = np.zeros(pow(n, 2))
    r = np.matmul(A, x)
    r = b - r
    iterations = 0

    for i in range(1, max_iterations):
        iterations += 1
        z = np.linalg.solve(A, r)
        alpha = 1
        if i == 1:
            p = z
            alpha = 1 / d
        elif i == 2:
            beta = (1 / 2) * (c * alpha) ** 2
            alpha = 1 / (d - beta / alpha)
            p = z + beta * p
        else:
            beta = (c * alpha / 2) ** 2
            alpha = 1 / (d - beta / alpha)
            p = z + beta * p
        x = x + alpha * p
        r = np.matmul(A, x)
        r = b - r
        if norm(r) < eps:
            return [x, iterations]
    return [x, iterations]


def create_matrix_A(n=10):
    A = np.zeros((n ** 2, n ** 2))
    for i in range(n ** 2):
        A[i][i] = -4
        if i - 1 >= 0:
            A[i-1][i] = 1.0
        if i + 1 < n ** 2:
            A[i+1][i] = 1.0
        if i - n >= 0:
            A[i-n][i] = 1.0
        if i + n < n ** 2:
            A[i+n][i] = 1.0
    return A


def print_matrix(A, n=10):
    for i in range(n):
        for j in range(n):
            print(A[i][j], " ", end='')
        print("")


A = create_matrix_A()
# print_matrix(A, 25)


def create_vector_b(n=10):
    phi = lambda x, y: (x + y)/2
    b = np.zeros(n**2)
    idx = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            b[idx] = phi(j, i)
            idx += 1
    return b


b = create_vector_b()
# print(b)


[res, iter_count] = chebyshev(A, b, 1000, 0, 2, 1e-12)
print("Ilości iteracji dla metody czebyszewa wynosi : {}".format(iter_count))
print("Rozwiazanie :")
print(res)