import numpy as np

def oneDimArray(size):
    return np.arange(size)

def twoDimArray(size, rows, columns):
    return np.arange(size).reshape(rows,columns)

def randomVector(min, max, length):
    return np.random.randint(low=min, high=max, size=length)

def randomMatrix(min, max, rows, columns):
    return np.random.randint(low=min, high=max, size=(rows,columns))

def identityMatrix(size):
    return np.identity(size, dtype=int)

print(randomVector(0,10,10), "\n")
print(randomMatrix(0,10,4,4),"\n")
print(twoDimArray(15,3,5),"\n")
print(identityMatrix(5),"\n")
print(oneDimArray(10))
