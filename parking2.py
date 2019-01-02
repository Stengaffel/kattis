import sys

def bubble_sort(x):
    for i in range(0,len(x)):
        for j in range(0,len(x)-1-i):
            if x[j] > x[j+1]:
                temp = x[j]
                x[j] = x[j+1]
                x[j+1] = temp
    return x

test_cases = int( sys.stdin.readline() )

runs = 0
for i in sys.stdin:
    i = int( i )

    streets = [ int(r) for r in sys.stdin.readline().split() ]
    streets = bubble_sort(streets)
    start = streets[0]

    dist = 0
    cur_n = start

    for s in streets:
        dist = dist + s - cur_n
        cur_n = s
    dist = dist + ( cur_n - start )

    print('{}'.format(dist))

    runs = runs + 1
    if runs == test_cases:
        break