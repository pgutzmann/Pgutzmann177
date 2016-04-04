import numpy as np
import matplotlib.pyplot as plt

print 'This program will calculate the time it takes for a ball to reach the'
print 'the ground when thrown with a range of initial velocities from a 800'
print 'meter tall tower'
print 'Assume down is the psotive direction'

a       = 9.81 / 2.     #gravity constant divided by 2, will be used for quadratic
c       = 800.          #height of the tower
vrange  = []            #range of user enetered initial velocities
time    = []
vel_num = 0             
 
#getting user input
vmin = float(input('Please enter a minimum velocity (m/s): '))
vmax = float(input('Please enter a maximum velocity (m/s): '))
while (vmin > vmax):
    vmin = float(input('Please enter a minimum velocity less than maximum velocity: '))

#getting the range between vmin and vmax in 10 increments
dy = (vmax - vmin) / 9.
for vel_num in range(10):
    vrange.append(vel_num*dy + vmin)
print 
print 'Velocity range in 10 increments:'
print vrange

#calculating time to the ground
vel_num = 0
while vel_num < 10:
    temp1 = vrange[vel_num]**2 + 4*a*c
    temp2 = np.sqrt(temp1)
    temp3 = (-vrange[vel_num] + temp2) / (2*a)
    time.append(temp3)
    vel_num += 1
print 
print 'Time to the ground with 10 different inital velocities:'
print time

np.array(time)
np.savetxt('ParkerGutzmannTime.txt', time)

plt.plot(vrange, time)
plt.xlabel("Initial Velocity (m/s)")
plt.ylabel("Time to Reach Ground (s)")
plt.title("Time vs. Initial Velocity")
plt.savefig('ParkerGutzmanntime.png')