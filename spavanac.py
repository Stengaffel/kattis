import sys

a = sys.stdin.readline()
a = a.split()

h = int(a[0])
min = int(a[1])

if ( min >= 45 ):
    print("{} {}".format(h, min-45))
else:
    min = 60 - (45 - min)
    if( h == 0 ):
        h = 23
    else:
        h = h - 1
    print("{} {}".format(h,min))
