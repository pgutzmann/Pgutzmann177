### This program will integrate an array with trapezoidal rule and simpsons rule

### Trapezoidal rule
def trapezoidal(time, velocity):
    a = 0           #####this represents the index of the vectors
    I = 0.0
    
    for a in range(0,(len(time)-1)):
        I += (velocity[a] + velocity[a+1]) * 0.5 * (time[a+1] - time[a])
    
    return I

### Simpsons rule
def simpsons(time, velocity):
    a = 0
    I = 0.0
    
    while a < (len(time)-2):
        dx = (time[a+1] - time[a]) ###this assumes there is equal spacing between each value
        I += (velocity[a] + (4*velocity[a+1]) + velocity[a+2]) * dx / 3. 
        a += 2
        
    return I

