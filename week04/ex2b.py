### this program will find the roots of a polynomial
import numpy as np
### defining function and the derivative of the function
def f(x):
    return 924.*x**6. - 2772.*x**5. + 3150.*x**4. - 1680.*x**3. + 420.*x**2. - 42.*x + 1.

def fprime(x):
    return 5544.*x**5. - 13860.*x**4. + 12600.*x**3. - 5040.*x**2. + 840.*x - 42.

### initializing variables
delta = 1
guess = [0.,0.2,0.4,0.6,0.8,1.0]

### newtons equation
def newtons(x):
    delta = 1.
    
    while np.abs(delta) > 10**-10:
        delta = (f(x) / fprime(x))
        x    -= delta
    return x

### different initial guesses to get all the roots    
for i in range(len(guess)):
    x = newtons(guess[i])
    print 'Initial guess:',guess[i]
    print 'Root Value:   ', x , '\n'
    