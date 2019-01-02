import sys

for i in sys.stdin:
    N = int(i)
    for k in range(1,N+1):
        print("{} Abracadabra".format(k))
