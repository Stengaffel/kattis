import sys
import math

test_cases = int( sys.stdin.readline() )

runs = 0
for i in sys.stdin:
    i = str(i).strip()
    n = int( math.sqrt( len(i) ) )
    m = []
    ind = 0
    # Enter coded message into matrix
    for row in range( 0, n ):
        m.append([])
        for col in range( 0, n ):
            m[row].append(i[ind])
            ind = ind + 1
    
    message = ''
    for col in range( n-1, -1, -1):
        for row in range(0, n):
            message = message + m[row][col]
    print('{}'.format(message))
    runs = runs + 1
    if runs == test_cases:
        break