import numpy as np
from numpy.fft import rfft2,irfft2
import matplotlib.pyplot as plt

### Plotting the original blurred image
plt.figure(1)
blur = np.loadtxt('blur.txt')
plt.imshow(blur,cmap='gray')
plt.savefig('ParkerGBlur.png')

### Defining the gausian function
def gaussian(rsquared, sigma):
    return np.exp(- float(rsquared) / (2.*sigma**2))

###Some constants
npix = len(blur)
psf = np.zeros((npix,npix))
sigma = 25.
orgin = npix / 2
e = 10**(-3)

### creating the gaussian and centering it at the orgin
for i in range(npix):
    for j in range(npix):
        rsquared = (i - orgin)**2 + (j - orgin)**2
        psf[i,j] = gaussian(rsquared,sigma)
        
psf = np.roll(psf,512,0)
psf = np.roll(psf,512,1)
    
###Plotting the gaussian    
plt.figure(2)
plt.imshow(psf, cmap='gray')
plt.savefig('ParkerGPSF.png')

###Getting the fourrier coeficients
blurtrans = rfft2(blur)
psftrans = rfft2(psf)


### Creating the unblurred coeficients
k = 0
for k in range(1024):
    for l in range(512):
        if (psftrans[k,l]) < e:
            blurtrans[k,l] = blurtrans[k,l]

        else:
            blurtrans[k,l] /= psftrans[k,l]
        
        
### Doing the inverse fourier transforms and plotting the clear picture
clear = irfft2(blurtrans)
plt.figure(3)
plt.imshow(clear, cmap='gray')
plt.savefig('ParkerGClear.png')