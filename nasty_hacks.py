import sys

limit = int(sys.stdin.readline())

noAdv = []
adv = []
cost = []

for i in sys.stdin:
    i = i.split()
    noAdv.append(int(i[0]))
    adv.append(int(i[1]))
    cost.append(int(i[2]))
    if len(noAdv) == limit:
        break

for k in range(0,len(noAdv)):
    advRev = int(adv[k] - cost[k])
    if advRev == noAdv[k]:
        print("does not matter")
        continue
    if advRev > noAdv[k]:
        print("advertise")
        continue
    if advRev < noAdv[k]:
        print("do not advertise")
        continue
