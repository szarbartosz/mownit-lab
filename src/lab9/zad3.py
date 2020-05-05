import copy
import time
from random import randrange
import numpy as np
import matplotlib.pyplot as plt
from lab9.zad1 import gauss_elimination, gauss_elimination_pivoting


def randomVector(n):
    return np.random.rand(n)


def randomMatrix(n):
    return np.random.rand(n, n)


def measure_time():
    n = randrange(100, 420)
    A = randomMatrix(n).tolist()
    B = randomVector(n).tolist()

    start = time.time()
    gauss_elimination(copy.deepcopy(A), copy.deepcopy(B))
    stop = time.time()
    gauss = stop - start

    start = time.time()
    gauss_elimination_pivoting(copy.deepcopy(A), copy.deepcopy(B))
    stop = time.time()
    gauss_pivoting = stop - start

    return gauss, gauss_pivoting, n

if __name__ == '__main__':
    gauss = []
    gauss_pivoting = []
    size = []
    for i in range(100):
        gauss_time, gauss_pivoting_time, n = measure_time()
        gauss.append(gauss_time)
        gauss_pivoting.append(gauss_pivoting_time)
        size.append(n)

    for i in range(100):
        f = open("file.txt", "a")
        f.write(f"matrix size: {size[i]} \t gauss elimination: {gauss[i]}[s] \t gauss elimination with pivoting: {gauss_pivoting[i]}[s]"'\n')
        f.close()

    plt.plot(size, gauss, 'g.', label="gauss")
    plt.plot(size, gauss_pivoting, 'r.', label="gauss pivoting")
    plt.xlabel("matrix size")
    plt.ylabel("time[s]")
    plt.title("gauss elimination time measurement")
    plt.legend()
    plt.grid(True)
    plt.savefig("gauss_plot")
    plt.show()