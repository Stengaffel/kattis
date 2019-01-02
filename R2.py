import sys

for i in sys.stdin:
    ab = i.split()
    R1 = int(ab[0])
    M = int(ab[1])

    R2 = 2*M - R1
    print(R2)
