import numpy as np
import scipy
import ex1 as int


## Inputing function
def f(x):
    f = x**4 - (2*x) + 1
    return f
    
##turning the function into an array
def FunctToArray(xmin, xmax, num_bin):
    xlist = []
    ylist = []
    dx    = 0.0   ### size of the slice
    i     = 0    ### placeholder
    
    dx  = float(xmax - xmin) / num_bin
    
    #getting the array for x values
    while i < num_bin + 1:
        xlist.append(xmin + (i*dx))
        i += 1
    
    #getting the array for y values
    i = 0
    while i < num_bin + 1:
        ylist.append(f(xmin + (i*dx)))
        i += 1
    
    return xlist, ylist


xlist = []
ylist = []
realValue = (32./5.) - 4. + 2.     ### the actual value of the integral

### inputing parameters to turn function into an array
xlist, ylist = FunctToArray(0,2,20)

### finding the area unde the curve
trap1 = int.trapezoidal(xlist,ylist)
simp1 = int.simpsons(xlist,ylist)  

### intrinsic functions in python    
trap2 = np.trapz(ylist,xlist)
simp2 = scipy.integrate.simps(ylist,xlist)


print 'This is my value using trapezoidal rule: ' + str(trap1)
print 'This is the value using the intrinsic trapezoidal function: ' + str(trap2) + '\n'
print 'This is my value using simpsons rule: ' + str(simp1)
print 'This is the value using the intrinsic simpsons rule: ' + str(simp2) + '\n'

### recomputing trapezoidal and simpson rule using 10 bins
xlist, ylist = FunctToArray(0,2,10)

trap_10 = int.trapezoidal(xlist,ylist)
simp_10 = int.simpsons(xlist,ylist)

#Getting the error of each method
errortrap = (trap_10 - trap1) / 3
errorsimp = (simp_10 - simp1) / 15
print 'This is the error for trapezoidal rule: ' + str(errortrap)
print 'This is the error for simpsons rule: ' + str(errorsimp) + '\n'
print 'This is the actual value of the integral: ' + str(realValue)