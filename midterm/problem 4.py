import matplotlib.pyplot as plt
import numpy as np

def potential(r):
    k = 9. *10.**9.
    Q = -1
    return k * Q / (r + 10.**(-10.))

npix = 100
xpos = float(npix / 2.)
ypos = float(npix / 2.)

array = np.zeros([npix,npix])
    
for i in range(npix - 1):
    for j in range(npix - 1):
        y = j - ypos
        x = i - xpos
        r = (y**2 +x**2)**0.5
        
        array[i,j] = potential(r)

plt.imshow(array)
plt.savefig("problem4.png")