import numpy as np
import matplotlib.pyplot as plt

xarray = np.linspace(0, 1, 1000)
yarray = []
N      = 1000

def wave():
    N = 1000
    yarray = []
    
    for i in range(N):
        yarray.append(np.sin(np.pi * i / float(N)) * np.sin(20. * np.pi * i / float(N)))
        
    return yarray

def dft(y):
    N = 1000
    c = np.zeros(N//2 + 1,complex)
    for k in range(N//2 + 1):
        for n in range(N):
            c[k] += y[n] * np.exp(- 2.j * np.pi * k * n / N)
    return c


yarray = wave()
coeff = dft(yarray)
num_coeff = len(dft(yarray))

plt.subplot(2,1,1)
plt.plot(np.arange(num_coeff), np.abs(coeff))
plt.title('Coefficients')
plt.xlim(0,100)

plt.subplot(2,1,2)
plt.plot(xarray, yarray)
plt.title('Modulated Sine Wave')
plt.tight_layout()