import numpy as np
from lab12.zad1 import chebyshev, create_matrix_A, create_vector_b


def gauss_seidl(A, b, max_iterations):
    iterations = 0
    x = np.zeros(len(b))
    for i in range(max_iterations):
        iterations += 1
        x_new = np.zeros_like(x)
        for i in range(A.shape[0]):
            s1 = np.dot(A[i, :i], x_new[:i])
            s2 = np.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]
        if np.allclose(x, x_new, rtol=1e-12):
            break
        x = x_new
    return x, iterations

def sor(A, b, max_iterations, omega):
    iterations = 0
    epsilon = 1e-12
    x = np.zeros_like(b)
    if omega < 0 or omega > 2:
        print('omega < 0 or omega > 2')
        return [x, -1]
    n = b.shape
    x_new = np.zeros_like(x)
    for _ in range(max_iterations):
        iterations += 1
        for i in range(n[0]):
            new_values_sum = np.dot(A[i, :i], x[:i])
            old_values_sum = np.dot(A[i, i + 1:], x_new[i + 1:])
            x[i] = (b[i] - (old_values_sum + new_values_sum)) / A[i, i]
            x[i] = np.dot(x[i], omega) + np.dot(x_new[i], (1 - omega))
        if np.linalg.norm(np.dot(A, x) - b) < epsilon:
            break
        x_new = x
    return x, iterations


A = create_matrix_A()
b = create_vector_b()


def compare(A, b, max_iterations, l_max, l_min, epsilon, omega):
  chebyshev_result, chebyshev_iterations = chebyshev(A, b, max_iterations, l_max, l_min, epsilon)
  gauss_seidl_result, gauss_seidl_iterations = gauss_seidl(A, b, max_iterations)
  sor_result, sor_iterations = sor(A, b, max_iterations, omega)

  print(f"Chebyshev result: \n {chebyshev_result}, \n")
  print(f"Gaus-Seidl result: \n {gauss_seidl_result}, \n")
  print(f"SOR result: \n {sor_result}, \n")

  print(f"Chebyshev iterations: {chebyshev_iterations}")
  print(f"Gaus-Seidl iterations: {gauss_seidl_iterations}")
  print(f"SOR iterations: {sor_iterations}")


compare(A, b, 1000, 0, 2, 1e-12, 1.2)


import matplotlib.pyplot as plt
import matplotlib

n = 10
chebyshev_result, chebyshev_iterations = chebyshev(A, b, 1000, 0, 2, 1e-12)
cmap = matplotlib.cm.prism

x = []
y = []
for i in range(1, n+1):
    for j in range(1, n+1):
        x.append(i)
        y.append(j)
sizes = [1200 for i in range(100)]

plt.scatter(x, y, c=chebyshev_result, sizes=sizes, alpha=0.8, cmap=cmap)
plt.colorbar()
plt.show()