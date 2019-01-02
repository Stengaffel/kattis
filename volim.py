import sys

K = int( sys.stdin.readline() )

turns = int( sys.stdin.readline() )

time = 0
exploded = False
loser = 0

runs = 0
for i in sys.stdin:
    i = i.split()
    T = int( i[0] )
    res = str( i[1] ).strip()

    time = time + T
    if time >= 210 and exploded == False:
        exploded = True
        loser = K
    
    if res == 'T':
        K = K + 1
        if K >= 9:
            K = 1

    runs = runs + 1
    if runs == turns:
        break

print('{}'.format(loser))