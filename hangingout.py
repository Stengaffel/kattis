import sys

base = [ int(x) for x in sys.stdin.readline().split() ]

cur = 0
denied = 0

runs = 0
for i in sys.stdin:
    i = i.split()
    com = str(i[0])
    amount = int(i[1])

    if com == 'enter':
        if cur + amount > base[0]:
            denied = denied + 1
        else:
            cur = cur + amount
    else:
        cur = cur - amount
    runs = runs + 1
    if runs == base[1]:
        break

print('{}'.format(denied))