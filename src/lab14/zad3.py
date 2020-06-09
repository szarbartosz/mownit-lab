import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy import fft


rate, data = wavfile.read('time_solo.wav')
samples_no = len(data)
normalized_data = data / (2.**15)
time = np.arange(0, float(samples_no), 1) / rate
plt.rcParams['figure.figsize'] = [20, 5]
plt.plot(time, normalized_data, linewidth=0.2, alpha=0.6, color='#0462b0')
plt.xlabel('time (s)')
plt.ylabel('amplitude')
plt.grid()
plt.show()
plt.savefig('time_solo.png')


T = 1.0 / samples_no
yf = fft.fft(normalized_data)
xf = np.linspace(0.0, 1.0 / (2.0*T), samples_no // 2)
plt.plot(xf, np.abs(yf[0:samples_no // 2]))
plt.grid()
plt.show()
plt.savefig('time_solo_fft.png')


for i in range(len(xf)):
    if 8000 < xf[i] < 16000:
        yf[i] = 0

plt.plot(xf, np.abs(yf[0:samples_no // 2]))
plt.grid()
plt.show()
plt.savefig('time_solo_remove.png')


ifft = np.real(fft.ifft(yf))
wavfile.write("time_solo_ifft.wav", len(ifft), ifft)

plt.plot(time, ifft)
plt.xlabel('time (s)')
plt.ylabel('amplitude')
plt.grid()
plt.show()
plt.savefig('time_solo_ifft.png')