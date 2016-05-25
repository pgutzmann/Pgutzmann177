import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

N = 1000
xarray = np.linspace(0, 1, 1000)
yarray = signal.sawtooth(xarray * 2. * 2. * np.pi)


def dft(y):
    N = 1000
    c = np.zeros(N//2 + 1,complex)
    for k in range(N//2 + 1):
        for n in range(N):
            c[k] += y[n] * np.exp(- 2.j * np.pi * k * n / N)
    return c

coeff = dft(yarray)
num_coeff = len(dft(yarray))

plt.subplot(2,1,1)
plt.plot(np.arange(num_coeff), np.abs(coeff))
plt.title('Sawtooth Wave Coefficients')
plt.xlim(0,100)

plt.subplot(2,1,2)
plt.plot(xarray, yarray)
plt.title('Sawtooth Wave')
plt.tight_layout()