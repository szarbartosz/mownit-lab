import time
from math import sqrt
from random import randrange
import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
from scipy import linalg


def crout(A):
    n = len(A)
    L = [[0] * n for i in range(n)]
    U = [[0] * n for i in range(n)]

    for j in range(n):
        U[j][j] = 1
        for i in range(j, n):
            tmp_l = float(A[i][j])
            for k in range(j):
                tmp_l -= L[i][k] * U[k][j]
            L[i][j] = tmp_l
        for i in range(j + 1, n):
            tmp_u = float(A[j][i])
            for k in range(j):
                tmp_u -= L[j][k] * U[k][i]
            if int(L[j][j]) == 0:
                raise ZeroDivisionError('attempted to divide by 0')
            U[j][i] = tmp_u / L[j][j]
    return L, U


def doolittle(A):
    n = len(A)
    L = [[0] * n for i in range(n)]
    U = [[0] * n for i in range(n)]

    for i in range(n):
        L[i][i] = 1

        for k in range(i, n):
            sum = 0
            for j in range(i):
                sum += (L[i][j] * U[j][k])

            U[i][k] = A[i][k] - sum

        for k in range(i, n):
            sum = 0
            for j in range(i):
                sum += (L[k][j] * U[j][i])

            L[k][i] = (A[k][i] - sum) / U[i][i]

    return L, U


def cholesky(A):
    n = len(A)
    L = [[0] * n for i in range(n)]

    for i in range(n):
        for k in range(i + 1):
            tmp_sum = sum(L[i][j] * L[k][j] for j in range(k))

            if i == k:
                L[i][k] = sqrt(A[i][i] - tmp_sum)
            else:
                L[i][k] = (1.0 / L[k][k] * (A[i][k] - tmp_sum))
    return L, np.array(L).transpose()


def random_matrix(low, high, n):  # return random symmetric and positive matrix
    A = np.random.randint(low, high, size=(n, n))
    return np.dot(A, A.transpose()), np.random.randint(low, high, size=(n, 1))


def decompose_and_solve(A, Y, method):
    L, U = method(A)
    z = np.linalg.solve(L, Y)
    x = np.linalg.solve(U, z)
    return x


def measure_time():
    n = randrange(20, 100)
    A, b = random_matrix(40, 160, n)

    start = time.time()
    decompose_and_solve(A, b, crout)
    stop = time.time()
    crout_time = stop - start

    start = time.time()
    decompose_and_solve(A, b, doolittle)
    stop = time.time()
    doolittle_time = stop - start

    start = time.time()
    decompose_and_solve(A, b, cholesky)
    stop = time.time()
    cholesky_time = stop - start

    start = time.time()
    np.linalg.solve(A, b)
    stop = time.time()
    numpy_time = stop - start

    start = time.time()
    sc.linalg.solve(A, b)
    stop = time.time()
    scipy_time = stop - start

    return crout_time, doolittle_time, cholesky_time, numpy_time, scipy_time, n


if __name__ == '__main__':
    crout_tab = []
    doolittle_tab = []
    cholesky_tab = []
    numpy_tab = []
    scipy_tab = []
    size = []
    for i in range(100):
        crout_time, doolittle_time, cholesky_time, numpy_time, scipy_time, n = measure_time()
        crout_tab.append(crout_time)
        doolittle_tab.append(doolittle_time)
        cholesky_tab.append(cholesky_time)
        numpy_tab.append(numpy_time)
        scipy_tab.append(scipy_time)
        size.append(n)

    for i in range(100):
        f = open("file_2.txt", "a")
        f.write(f"matrix size: {size[i]} \t crout: {crout_tab[i]}[s] \t doolittle: {doolittle_tab[i]}[s] \t cholesky: {cholesky_tab[i]}[s] \t numpy: {numpy_tab[i]}[s] \t scipy: {scipy_tab[i]}[s]"'\n')
        f.close()

    plt.plot(size, crout_tab, 'g.', label="crout method")
    plt.plot(size, doolittle_tab, 'r.', label="doolitle method")
    plt.plot(size, cholesky_tab, 'b.', label="cholesky method")
    plt.plot(size, numpy_tab, 'c.', label="numpy method")
    plt.plot(size, scipy_tab, 'm.', label="scipy method")
    plt.xlabel("matrix size")
    plt.ylabel("time[s]")
    plt.title("czas faktoryzacji LU")
    plt.legend()
    plt.grid(True)
    plt.savefig("LU_2")
    plt.show()