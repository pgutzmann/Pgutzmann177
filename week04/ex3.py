### this program will find the roots of a function using secant method
import numpy as np
import matplotlib.pyplot as plt
import scipy

### defining function
def f(x):
    return x**2 - (4*x*np.sin(x)) + (2*np.sin(x))**2

### Printing a graph to find intitila guesses
xvals = np.linspace(0,3,100)
yvals = f(xvals)
plt.plot(xvals,yvals)

## initial guesses
x1 = [0.6,2.2]
x2 = [0.5,2.0]

def secant(x1,x2):
    error = 1.
    
    while np.abs(error) > 10.**(-20.):
        x3 = x2 - ((f(x2) * (x2-x1)) / (f(x2)-f(x1)))
        x1 = x2
        x2 = x3
        error = x1 - x2
    
    return x3
    
### printing my solutions and the intrinsic function solutions    
print 'Assuming zero is a positive root\n'
for i in range(len(x1)):
    solution = secant(x1[i], x2[i])
    print 'My x value for a root:     ' + str(solution)
    solution = scipy.optimize.fsolve(f,x1[i])
    print 'Inrinsic vaule for a root: ' + str(solution[0]) + '\n'
    
    
