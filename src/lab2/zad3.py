import numpy as np

def containsZero(vector):
    print('indexes of "0" elements:', np.where(vector == 0))

def containsInf(vector):
    print('indexes of "inf" elements', np.where(vector == np.inf))
    print('indexes of "-inf" elements', np.where(vector == -np.inf))

def compare(x, y):
    print("first vector/matrix:\n", x)
    print("second vector/matrix:\n", y)
    if x.ndim == y.ndim and a.size == b.size:
        print("comparison result:")
        print(np.equal(x,y))
    else:
        print("compared vectors/matrices have different dimensions or have differenet number of elements")

a = np.array([1,2,3,4,5,6,7,8,9])
b = np.array([1,8,3,4,5,6,7,2,9])
c = np.array([-np.inf,2,3,4,0,6,7,8,np.inf])

d = np.matrix('1 2 3; 4 5 6; 7 8 9')
e = np.matrix('1 8 3; 4 5 6; 7 3 9')
f = np.matrix('1 2 3; 4 0 6; 7 8 9')


compare(a,b)
compare(d,e)
containsZero(c)
containsInf(c)
containsZero(f)