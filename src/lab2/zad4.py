import numpy as np

def byteSize(ndarray):
    print("size of vector/matrix in bytes: ", ndarray.nbytes)
    print("size of singular element: ", ndarray.itemsize)

a = np.array([1.5,2,3,4,5,6,7,8,9])
d = np.matrix('1 2 3; 4 5 6; 7 8 9')
print(a)
byteSize(a)
print("\n",d)
byteSize(d)