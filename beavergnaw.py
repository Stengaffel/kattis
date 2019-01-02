import sys
import math

for i in sys.stdin:
    i = [int(x) for x in i.split()]
    if i[0] == 0 and i[1] == 0:
        break

    D = i[0]
    V = i[1]

    d =  ( D**3 - 6 * (V / math.pi) ) ** (1/3)

    print('{}'.format(d))