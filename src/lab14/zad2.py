from scipy import fft
import matplotlib.pyplot as plt
from random import random
import numpy as np

# liczba próbek
N = 1000
F = 8
ft = []
t = np.linspace(0.0, 1.0, N)


#1. Wypełnienie tablicy wartościami funkcji sinus ("sygnał") zaburzonej niewielkim "szumem"
for i in t:
    ft.append(np.sin(np.sin(2*np.pi*i*F) + random()))


#2. Wykres zaszumionej funkcji
plt.plot(t, ft)
plt.grid()
plt.show()


#3. FFT + wykres
T = 1.0 / N
yf = fft.fft(ft)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
y = np.abs(yf[0:N//2])
plt.plot(xf, 2.0/N * y)
plt.grid()
plt.show()