import sys

totSum = 0
biggestPers = 0

pers = 1

for i in sys.stdin:
    i = i.split()
    curSum = 0
    for p in i:
        curSum = curSum + int(p)
    if curSum > totSum:
        totSum = curSum
        biggestPers = pers
    if pers == 5:
        break
    pers = pers + 1

print("{} {}".format(biggestPers,totSum))
