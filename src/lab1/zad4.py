import numpy as np
from bitstring import BitArray

def differentPrecision(num, bits):
  binum = BitArray(float=num, length=bits)
  sign = int(binum[0])
  if bits == 32:
    exponent = binum[1:9].bin
    mantissa = binum[9:].bin
  else:
    exponent = binum[1:12].bin
    mantissa = binum[12:].bin
  return sign, exponent, mantissa

def displayPrecision(num):
  binum = BitArray(float=num, length=64)
  sign = int(binum[0])
  exponent = binum[1:12].bin
  mantissa = binum[12:].bin
  return sign, exponent, mantissa

print("float16:", displayPrecision(np.float16(1/3)))
print("float32:", displayPrecision(np.float32(1/3)))
print("float64:", displayPrecision(np.float64(1/3)))
print('\n')
print("float16 to float32:", displayPrecision(np.float32(np.float16(1/3))))
print("float16 to float64:", displayPrecision(np.float64(np.float16(1/3))))
print("float32 to float64:", displayPrecision(np.float64(np.float32(1/3))))