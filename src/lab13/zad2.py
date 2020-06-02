from numpy import random
import matplotlib.pyplot as plt

arr = []

for _ in range(100):
  arr.append(random.random())

x = [arr[i] for i in range(len(arr)) if i % 2 == 0]
y = [arr[i] for i in range(len(arr)) if i % 2 == 1]

plt.figure(figsize=(10, 10), dpi=60)
plt.scatter(x, y)
plt.show()