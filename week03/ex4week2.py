import numpy as np

def f(x):
    f = np.sin(np.sqrt(100*x))**2
    return f
    
e           = 100. # cause why not
xmin        = 0.
xmax        = 1.
numbins     = 1.
adaptiveint = 0.
summation   = 0. 
ylist       = [f(0),f(1)]
trap        = np.trapz(ylist) #integral with one slice


while (e > 10**(-6)):
    numbins  *= 2.
    dx        = (xmax - xmin) / numbins
    summation = 0.
    
    ### finding the summation of the odd terms
    i = 1
    while (i <= numbins - 1):
        summation += f(xmin + i*dx)
        i += 2
    
    ### finding the new integral value and error
    adaptiveint = (.5*trap) + (dx*summation)
    e           = np.abs((adaptiveint - trap) / 3.)
    trap        = adaptiveint
    
print 'This is the value of the integral:', trap
print '\nThis is the error:',e
