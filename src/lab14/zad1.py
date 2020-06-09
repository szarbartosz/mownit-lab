from scipy import fft
import matplotlib.pyplot as plt
import numpy as np

# liczba próbek
N = 1000
t = np.linspace(0.0, 1.0, N)


def generate_and_visualize(F, ft=0):
    for i in range(len(F)):
        ft += np.sin(2 * np.pi * t * F[i])
    plt.plot(t, ft)
    plt.grid()
    plt.show()
    return ft


def analyze(ft):
    T = 1.0 / N
    yf = fft.fft(ft)
    xf = np.linspace(0.0, 1.0 / (2.0 * T), N // 2)
    plt.plot(xf, 2.0 / N * np.abs(yf[0:N // 2]))
    plt.grid()
    plt.show()


print('2 składowe:')
F2 = [8, 16]
ft2 = generate_and_visualize(F2)
analyze(ft2)

print('4 składowe:')
F4 = [8, 16, 32, 64]
ft4 = generate_and_visualize(F4)
analyze(ft4)

print('8 składowych:')
F8 = [8, 16, 32, 64, 128, 256, 512, 1024]
ft8 = generate_and_visualize(F8)
analyze(ft8)
