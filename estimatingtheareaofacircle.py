import sys
import math

for i in sys.stdin:
    i = i.split()

    r = float( i[0] )
    m = int( i[1] )
    c = int( i[2] )

    if r == 0 and m == 0 and c == 0:
        break

    actual_area = ( r ** 2 ) * math.pi
    estimated_area = ( ( r * 2 ) ** 2 ) * ( c / m )

    print('{} {}'.format(actual_area,estimated_area))