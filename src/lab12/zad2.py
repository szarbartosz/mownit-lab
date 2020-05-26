import numpy as np
from lab12.zad1 import create_matrix_A, create_vector_b

def lecture_matrix_A(n=10):
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

def lecture_vector_b(n=10):
    phi = lambda x, y: (x + y)/2
    b = np.zeros(n**2)
    idx = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            b[idx] = phi(j, i)
            idx += 1
    return b

def print_matrix(A, n=10):
    for i in range(n):
        for j in range(n):
            print(A[i][j], " ", end='')
        print("")

def print_vector(b):
  print(b)

A = create_matrix_A()
b = create_vector_b()

print("matrix A:")
print_matrix(A, 20)
print('\n')
print("vector b:")
print_vector(b)