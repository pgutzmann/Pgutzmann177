import numpy as np
import matplotlib.pyplot as plt

xarray = np.linspace(0,1,1000)
yarray = []
N      = 1000

###Making the square wave
def square():
    yarray = []
    for i in range(500):
        yarray.append(1.)
    for j in range(500):
        yarray.append(-1.)
    return yarray
    
### Discrete Fourier transform
def dft(y):
    N = 1000
    c = np.zeros(N//2 + 1,complex)
    for k in range(N//2 + 1):
        for n in range(N):
            c[k] += y[n] * np.exp(- 2.j * np.pi * k * n / N)
    return c


coeff     = dft(square())
num_coeff = len(coeff)

### Plotting Function and Coefficients
plt.subplot(2,1,1)
plt.plot(np.arange(num_coeff), np.abs(coeff))
plt.title('Square Wave Coefficients')
plt.xlim(0,100)

plt.subplot(2,1,2)
plt.plot(xarray, square())
plt.ylim(-1.5,1.5)
plt.title('Square Wave')
plt.tight_layout()
