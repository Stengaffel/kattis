import sys

ds = sys.stdin.readline().split()
d1 = int(ds[0])
d2 = int(ds[1])

vals = [0] * (d1 + d2)

for i in range(1,d1+1):
    for j in range(1,d2+1):
        vals[i+j-1] = vals[i+j-1] + 1

bigSum = 0
for v in vals:
    if v > bigSum:
        bigSum = v

for i in range(0, len(vals)):
    if vals[i] == bigSum:
        print(i+1)