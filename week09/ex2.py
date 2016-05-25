import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import rfft,irfft

data        = np.loadtxt('sunspots.txt')
month       = data[:,0]
num_sunspot = data[:,1]

### Plotting sunspots as a funtion of time
plt.figure(1)
plt.plot(month,num_sunspot)
plt.xlabel('Time in Months')
plt.ylabel('Number of Sunspots')
plt.title('Sunspots Vs. Time')

### this is my length of a cycle estimate
len_est = 500 / 4
print "Length of cycle estimate in months:", str(len_est)

### Preforming the fast fourier transform and finding the power spectrum
coeff = rfft(num_sunspot)
power = np.abs(coeff)**2.
k     = np.arange(len(power)) 

### Plotting the power spectrum versus K
plt.figure(2)
plt.plot(k, power)
plt.title('Power Spectrum')
plt.xlabel('K (Frequency)')
plt.ylabel('Power')
plt.xlim([0,100])
plt.ylim([0,8.7**10])  ###changing limits to see the picture better

### finding the max power at the non zero peak
h = np.max(power[10:]) 
for i in range(len(k)):
    if power[i] == h:
        kmax = k[i]
        print "This is the value of k to which the non-zero "\
        "peak corresponds:", str(kmax)

### finding the period that relates to the k value found        
print "This is period of the cycle in months:",\
 str(float(len(month)) / float(kmax))