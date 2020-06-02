import matplotlib.pyplot as plt


def quasi_random(a, c, m, seed):
    return (a * seed + c) % m


def generate(n, a, c, m, seed):
    result = []
    for _ in range(n):
        seed = quasi_random(a, c, m, seed)
        result.append(seed/m)
    return result


arr1 = generate(100, 1103515245, 12345, 2**32, 10)
x1 = [arr1[i] for i in range(len(arr1)) if i % 2 == 0]
y1 = [arr1[i] for i in range(len(arr1)) if i % 2 == 1]

plt.figure(figsize=(10, 10), dpi=60)
plt.scatter(x1, y1)
plt.show()


arr2 = generate(100, 1229, 1, 2048, 10)
x2 = [arr2[i] for i in range(len(arr2)) if i % 2 == 0]
y2 = [arr2[i] for i in range(len(arr2)) if i % 2 == 1]

plt.figure(figsize=(10, 10), dpi=60)
plt.scatter(x2, y2)
plt.show()


arr3 = generate(100, 1597, 51749, 24494, 10)
x3 = [arr3[i] for i in range(len(arr3)) if i % 2 == 0]
y3 = [arr3[i] for i in range(len(arr3)) if i % 2 == 1]

plt.figure(figsize=(10, 10), dpi=60)
plt.scatter(x3, y3)
plt.show()


arr4 = generate(100, 2**16 + 3, 0, 2**31, 10)
x4 = [arr4[i] for i in range(len(arr4)) if i % 2 == 0]
y4 = [arr4[i] for i in range(len(arr4)) if i % 2 == 1]

plt.figure(figsize=(10, 10), dpi=60)
plt.scatter(x4, y4)
plt.show()
