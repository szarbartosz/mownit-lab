import numpy as np
from bitstring import BitArray


def checkNormalization(number):
    binum = BitArray(float=number, length=32)
    if binum[1:9].bin == '00000000' and binum[9] == 0:
        x = 'de'
    else:
        x = ''
    print(number)
    print(f'Is {x}normalised', int(binum[0]), binum[1:9].bin, binum[9:].bin, '\n')


a = np.float32(1.1)
for i in range(0, 149):
    a = a/np.float32(2.0)
    checkNormalization(a)