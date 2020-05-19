import random
import numpy as np


def create_rand_matrix(min, max, N):
    A = np.zeros((N, N))
    for i in range(N):
        sum = 0
        for j in range(N):
            if j >= i: A[i][j] = A[j][i] = random.randint(min, max)
            if i != j: sum += abs(A[i][j])
        A[i][i] = sum
    return A


def create_rand_vector(min, max, N):
    return np.random.uniform(low=min, high=max + 1, size=(N,))


def gauss_seidel(A, b, max_iterations):
    x = np.zeros(len(b))
    for i in range(max_iterations):
        x_new = np.zeros_like(x)
        for i in range(A.shape[0]):
            s1 = np.dot(A[i, :i], x_new[:i])
            s2 = np.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]
        if np.allclose(x, x_new, rtol=1e-8):
            break
        x = x_new
    return x


def sor(A, b, omega, max_iterations, ):
    epsilon = 1e-8
    x = np.zeros_like(b)
    if omega < 0 or omega > 2:
        print('omega < 0 or omega > 2')
        return [x, -1]
    n = b.shape
    x_new = np.zeros_like(x)
    for _ in range(max_iterations):
        for i in range(n[0]):
            new_values_sum = np.dot(A[i, :i], x[:i])
            old_values_sum = np.dot(A[i, i + 1:], x_new[i + 1:])
            x[i] = (b[i] - (old_values_sum + new_values_sum)) / A[i, i]
            x[i] = np.dot(x[i], omega) + np.dot(x_new[i], (1 - omega))
        if np.linalg.norm(np.dot(A, x) - b) < epsilon:
            break
        x_new = x
    return x


A = create_rand_matrix(-30, 30, 8)
b = create_rand_vector(-20, 20, 8)
print("Solution: ", gauss_seidel(A, b, 1000))
print("Solution: ", sor(A, b, 0.2, 1000))


