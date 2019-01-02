import sys
import math

base = [int(x) for x in sys.stdin.readline().split()]
matches = []

for i in sys.stdin:
    matches.append(int(i))
    if( len(matches) == base[0] ):
        break
pyth = math.sqrt(base[1]**2 + base[2]**2)
for m in matches:
    if( m <= pyth ):
        print('DA')
    else:
        print('NE')
