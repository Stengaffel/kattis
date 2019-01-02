import sys
import math

for i in sys.stdin:
    i = [float(x) for x in i.split()]
    if i[0] == 0:
        break
    
    x1 = i[0]
    y1 = i[1]

    x2 = i[2]
    y2 = i[3]

    p = i[4]

    p_dist = ( math.fabs(x1-x2)**p+math.fabs(y1-y2)**p)**(1/p)
    print('{}'.format(p_dist))