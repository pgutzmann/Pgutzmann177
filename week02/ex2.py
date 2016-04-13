### using our functions to compute distance traveled
import matplotlib.pyplot as plt
import numpy as np
import ex1 as int

data     = np.loadtxt('velocities.txt')
time     = data[:,0]
velocity = data[:,1]

###Solving with data given
trap = int.trapezoidal(time, velocity)
simp = int.simpsons(time, velocity)

### extending the program to get a distance array
distance  = [0]
i         = 0
time2     = [time[0]]
velocity2 = [velocity[0]]

## actually solving for the distance array
while i < (len(time)-1):
    time2.append(time[i+1])
    velocity2.append(velocity[i+1])
    distance.append(int.trapezoidal(time2,velocity2))
    i += 1

## Plotting graphs
plt.subplot(2,1,1)
plt.plot(time, velocity)
plt.title('Velocity and Distance Vs. Time')
plt.xlabel('Time')
plt.ylabel('Velocity')

plt.subplot(2,1,2)
plt.plot(time, distance)
plt.xlabel('Time')
plt.ylabel('Distance')

### saving the results to a file
output1 = 'This is distance using trapezoidal rule: ' + str(trap) + '\n'
output2 = 'This is distance using simpsons rule: ' + str(simp) + '\n'

f = open('ParkerIntegralResults.txt', 'w+')
f.write(output1 + output2)
f.close()
