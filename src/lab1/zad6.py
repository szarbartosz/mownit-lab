import numpy as np
from tabulate import tabulate


def kahanAddition(num, n):
  sum = 0.0
  c = 0.0 #Poprawka zawierająca utracone niskie bity.
  for i in range(0, n):
    y = num - c
    t = sum + y #sum jest względnie duże w porównaniu z y co powoduje utratę bitów mniej znaczących liczby y
    c = (t - sum) - y #(t - sum) odzyskuje wyższe bity y, odjęcie y odzyskuje - (niższe bity y)
    sum = t
  return sum

def normalAddition(num, n, sum):
  for i in range(0, n):
    sum += num
  return sum


tab = [["float16", normalAddition(np.float16(0.6734914323452), 27684, np.float16(0))],
        ["float32", normalAddition(np.float32(0.6734914323452), 27684, np.float32(0))],
        ["float64", normalAddition(np.float64(0.6734914323452), 27684, np.float64(0))],
        ["kahan algorithm", kahanAddition(0.6734914323452, 27684)],
        ["Correct value:", 0.6734914323452*27684]]

print(tabulate(tab, headers=['type', 'value'], floatfmt=".10f"))