import numpy as np
import numpy.linalg as lin

Vplus = 5.
Vend  = 0.

print 'This is the system of equations we need to solve:'
str1 = ' 4V1 - V2 - V3 - V4 = ' + str(Vplus) + '\n'
str2 = '-V1 + 4V1 - V3 - V4 = ' + str(Vend)  + '\n'
str3 = '-V1 - V2 + 4V3 - V4 = ' + str(Vplus) + '\n'
str4 = '-V1 - V2 - V3 + 4V4 = ' + str(Vend) + '\n'
print str1 + str2 + str3 + str4

array  = np.array([[4,-1,-1,-1],[-1,4,-1,-1],[-1,-1,4,-1],[-1,-1,-1,4]], float)
equals = np.array([Vplus,Vend,Vplus,Vend], float)
length = len(equals)

for i in range(length):
    
    ###Making the diagnol terms 1
    divide      = array[i,i]
    array[i,:] /= divide
    equals[i]  /= divide
    
    ### making bottom values in column 0
    for j in range(i+1,length):
        multiply    = array[j,i]
        array[j,:] -= multiply*array[i,:]
        equals[j]  -= multiply*equals[i]
  
### back substitution      
V = np.zeros(length)

i = length - 1
while i > -1:
    V[i] = equals[i]
    
    j = i + 1
    while j < length:
        V[i] -= array[i,j] * V[j]
        
        j += 1
        
    i -= 1

intrinsicV = lin.solve(array,equals)

print 'These are the voltages I get:', V, '\n'
print 'Using the intrinsic function:', intrinsicV

