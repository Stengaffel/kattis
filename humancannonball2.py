import sys
import math

def computeY(v0,theta,x1):
    t = x1 / ( v0 * math.cos( math.radians(theta) ) )

    return ( v0 * t * math.sin( math.radians(theta) ) - 
                (1 / 2) * 9.81 * ( t ** 2 ) )

test_cases = int( sys.stdin.readline() )

v0 = []
theta = []
x1 = []
h1 = []
h2 = []

for i in sys.stdin:
    i = i.split()
    v0.append(float( i[0] ))
    theta.append(float( i[1] ))
    x1.append(float( i[2] ))
    h1.append(float( i[3] ))
    h2.append(float( i[4] ))
    if len(x1) == test_cases:
        break

for ind in range(0, len(x1)):
    y = computeY(v0[ind],theta[ind],x1[ind])
    if y > h1[ind] + 1 and y < h2[ind] - 1:
        print('Safe')
    else:
        print('Not Safe')

