import sys

coords = []

for i in sys.stdin:
    coords.append(int(i))

    if( len(coords) == 2 ):
        if( coords[0] > 1):
            if ( coords[1] > 1 ):
                print(1)
            else:
                print(4)
        else:
            if( coords[1] > 1 ):
                print(2)
            else:
                print(3)
