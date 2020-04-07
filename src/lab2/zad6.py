import time
import numpy as np
from tabulate import tabulate

def sumVectors(vec1, vec2):
    begin = time.time()
    result = []
    i = 0
    for val in vec1:
        result.append(val + vec2[i])
        i += 1
    end = time.time()
    return result, end - begin

def multiplyVectors(vec1, vec2):
    begin = time.time()
    result = 0
    i = 0
    for val in vec1:
        result += val * vec2[i]
        i += 1
    end = time.time()
    return result, end - begin

def multiplyMatrices(mat1, mat2):
    begin = time.time()
    rows1, columns1 = mat1.shape
    rows2, columns2 = mat2.shape
    result = np.zeros((rows1, columns2))
    for i in range(rows1):
        for j in range(columns2):
            for k in range(rows2):
                result[i][j] += mat1[i][k] * mat2[k][j]
    end = time.time()
    return result, end - begin

def sumVectorsNumpy(vec1, vec2):
    begin = time.time()
    result = np.add(vec1, vec2)
    end = time.time()
    return result, end - begin


def multiplyVectorsNumpy(vec1, vec2):
    begin = time.time()
    result = np.dot(vec1, vec2)
    end = time.time()
    return result, end - begin


def multiplyMatricesNumpy(mat1, mat2):
    begin = time.time()
    result = np.dot(mat1, mat2)
    end = time.time()
    return result, end - begin

a = np.array([8,2,3,4,5,6,7,8,9])
b = np.array([1,8,3,4,5,6,7,2,9])

c = np.array([[1,4,5], [5,3,2], [2,4,7]])
d = np.array([[2,6,8], [7,2,4], [3,6,8]])

table = [
        ['sum of vectors', sumVectors(a,b)[0], sumVectors(a,b)[1]],
        ['sum of vectors (Numpy)', sumVectorsNumpy(a,b)[0], sumVectorsNumpy(a,b)[1]],
        ['product of vectors', multiplyVectors(a,b)[0], multiplyVectors(a,b)[1]],
        ['product of vectors (Numpy)', multiplyVectorsNumpy(a,b)[0], multiplyVectorsNumpy(a,b)[1]],
        ['product of matrices',  multiplyMatrices(c,d)[0], multiplyMatrices(c,d)[1]],
        ['product of matrices (Numpy)',  multiplyMatricesNumpy(c,d)[0], multiplyMatricesNumpy(c,d)[1]]
        ]

print(tabulate(table, headers=['operation', 'result', 'time'], tablefmt="fancy_grid"))