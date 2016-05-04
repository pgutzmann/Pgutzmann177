import matplotlib.pyplot as plt
import numpy as np
import scipy

def y(t):
    return -3.*t**5. - 24.*t**4. + 3.*t + 10.
    
def yprime(t):
    return -15.*t**4. - 96*t**3 + 3.

n = 0
steps = 0
root = 0

xarray = np.linspace(0,10**9,20)
yarray = y(xarray)
plt.plot(xarray,yarray)

def newtons(t):
    error = 100
    n     = 0
    while np.abs(error) > 10.**(-10.):
        error = y(t) / yprime(t)
        t -= error
        n += 1
    return t,n
    
root,steps = newtons(10.**8.)
print "This is the value of the root: ",root
print "this is how many steps it took: ",steps
print scipy.optimize.fsolve(y, 10**8)