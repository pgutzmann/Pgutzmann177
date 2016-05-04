firstterm = 1
secondterm = 1
lastterm = 0

def fibonacci(i):
    firstterm = 1
    secondterm = 1
    lastterm = 0
    i -=2
    
    for j in range(i):
        lastterm = firstterm + secondterm
        firstterm = secondterm
        secondterm = lastterm
    return lastterm
    
print fibonacci(12)


ii = float(fibonacci(100)) / float(fibonacci(99))
print ii