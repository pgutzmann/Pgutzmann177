import numpy as np

print 'This program will calculate the time it takes for a ball to reach the'
print 'the ground when thrown from a 800 meter tall tower'

a = 9.81 / 2.     #gravity constant divided by 2
c = 800.       #height of the tower

#getting initial velocity from user
b = float(input('Enter an initial velocity for the ball with down being the positive direction: '))

#calculating the time using the quadratic formula
temp1 = b**2 + 4*a*c
temp2 = np.sqrt(temp1)
positive = (-b + temp2) / (2*a) # we don't use the root we get by subtracting
print positive, 'seconds'                  # because it will be negative
