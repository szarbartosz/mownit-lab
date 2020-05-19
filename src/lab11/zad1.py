import numpy as np
import random


def jacobi(A, b, max_iterations):
    D = np.diag(np.diag(A))
    LU = A - D
    epsilon = 1e-10
    x = np.zeros(len(b))
    for i in range(max_iterations):
        D_inv = np.diag(1 / np.diag(D))
        x_new = np.dot(D_inv, b - np.dot(LU, x))
        if np.linalg.norm(x_new - x) < epsilon:
            return x_new
        x = x_new
    return x


def random_matrix(min, max, n):
    A = np.zeros((n, n))
    for i in range(n):
        sum = 0
        for j in range(n):
            if j >= i:
              A[i][j] = A[j][i] = random.randint(min, max)
            if i != j:
              sum += abs(A[i][j])
        A[i][i] = sum
    return A


def random_vector(min, max, n):
    return np.random.uniform(low=min, high=max, size=(n,))


def compare(A, b, max_iterations):
  print("numpy result:")
  print(np.linalg.solve(A,b))
  print("Jacobi method result:")
  print(jacobi(A, b, max_iterations), '\n')