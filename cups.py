import sys

# Returns a sorted array from the array 'x
def bubble_sort(x):
    for i in range(0,len(x)):
        for j in range(0,len(x)-1-i):
            if x[j] > x[j+1]:
                temp = x[j]
                x[j] = x[j+1]
                x[j+1] = temp
    return x

test_cases = int( sys.stdin.readline() )

dict = {}
prel = []

for i in sys.stdin:
    i = i.split()
    # If first element is an integer
    if ord( str(i[0][0]) ) > 47 and ord( str(i[0][0]) ) < 58:
        dict[str( (1/2) * float( i[0] ) )] = str( i[1] )
        prel.append( (1/2) * float( i[0] ))
    # If first element is a string
    else:
        dict[str( float( i[1] ) )] = str( i[0] )
        prel.append(float( i[1] ))

    if len(prel) == test_cases:
        break

sorted = bubble_sort(prel)

for s in sorted:
    print("{}".format( dict[str(s)] ) )