### This program uses the relaxation method to find roots

### constants
a = 1.
b = 2.

### defining functions
def g(x):
    return b / (a + x**2)
    
def f(x):
    return g(x) * (a + x**2)

### initial guesses and solving for roots    
y = 10.
x = 10.
for i in range(5):
    y = g(x)
    x = f(x)
    
    print y,x

print 'I can''t make it not converge :('