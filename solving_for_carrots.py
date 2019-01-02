import sys

for i in sys.stdin:
    ab = i.split()
    if( len(ab) < 2 ):
        continue
    else:
        a = int(ab[0])
        b = int(ab[1])
        print(b)
        break
