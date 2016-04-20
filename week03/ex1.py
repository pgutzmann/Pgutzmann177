import numpy as np
import matplotlib.pyplot as plt

size       = 100.
npix       = 100
seperation = 10.
dx         = size / float(npix)
pi         = 3.14159
epsilon    = 8.854187817
q1         = 1.
q2         = -1.
phi1       = 0.
phi2       = 0.

### making grid
grid1 = np.zeros(shape = (npix,npix)).astype('float')
grid2 = np.zeros(shape = (npix,npix)).astype('float')

### position of the charges
q1xpos = (size / 2.) - (seperation / 2)
q1ypos = size / 2.
q2xpos = (size / 2.) + (seperation / 2)
q2ypos = size / 2.

### filling the grid with values
for j in range(npix):
    ypos = float(j) * dx
    
    for i in range(npix):
        xpos = float(i) * dx
        
        radius1 = np.sqrt((xpos - q1xpos)**2 + (ypos - q1ypos)**2)
        radius2 = np.sqrt((xpos - q2xpos)**2 + (ypos - q2ypos)**2)
        
        phi1 = q1 / (4. * pi * epsilon * radius1)
        phi2 = q2 / (4. * pi * epsilon * radius2)
        
        grid1[j,i] = phi1 + phi2

### making the plot
plt.subplot(2,1,1)
plt.imshow(grid1,origin='lower',extent=([0,size,0,size]))
plt.gray()
plt.xlabel('X (cm)')
plt.ylabel('Y (cm)')
plt.title('Electric Potential Density Graph')

### Making electric field magnitude grid
electricf = np.gradient(grid1)
grid2 = np.sqrt(electricf[0]**2+electricf[1]**2)

### plotting electric field magnitude
plt.subplot(2,1,2)
plt.imshow(grid2,origin='lower',extent=([0,size,0,size]))
plt.gray()
plt.xlabel('X (cm)')
plt.ylabel('Y (cm)')
plt.title('Electric Field Magnitude')
plt.tight_layout()
