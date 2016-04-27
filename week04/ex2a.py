import matplotlib.pyplot as plt
import numpy as np

### defining function
def f(x):
    return 924.*x**6. - 2772.*x**5. + 3150.*x**4. - 1680.*x**3. + 420.*x**2. - 42.*x + 1.

### making a plot
xval = np.linspace(0,1,100)
yval = f(xval)

plt.plot(xval,yval)
plt.title('Random Function')
plt.xlabel('X')
plt.ylabel('Y')
plt.text(.1,1,'Plotted with 100 bins')
plt.savefig('ParkerGutzmannPolynomial.png')