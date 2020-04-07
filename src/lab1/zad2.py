from bitstring import BitArray

def numParts(num):
    float64 = BitArray(float=num, length=64)
    print(float64.bin[0], " ", float64.bin[1:12], " ", float64.bin[12:63])
    if float64.bin[0]:
        print("znak: (+)")
    else:
        print("znak: (-)")
    print('cecha bin:', float64.bin[1:12])
    print('mantysa bin:', float64.bin[12:63])

    cecha = 0
    pow = 10
    for i in float64.bin[1:12]:
        if i == "1":
            cecha += 2 ** pow
        pow -= 1
    print('cecha dec:', cecha)

    mantysa = 0
    pow = -1
    for i in float64.bin[12:63]:
        if i == "1":
            mantysa += 2 ** pow
        pow -= 1
    print('mantysa dec:', mantysa, "\n")
    return float64


numParts(6 / 7)