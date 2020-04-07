import numpy as np
from lab1 import zad2

def numRange(num):
    arr = [np.nextafter(num, num - 1), num, np.nextafter(num, num + 1)]
    print(arr, "\n")
    print("number smaller than given number:")
    zad2.numParts(np.nextafter(num, num - 1))
    print("number grater than given number:")
    zad2.numParts(np.nextafter(num, num + 1))

numRange(6/7)