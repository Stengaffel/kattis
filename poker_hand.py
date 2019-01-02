import sys

a = [ str(x) for x in sys.stdin.readline().split() ]

checkArr = [0] * 13

for s in a:
    r = s[0]

    if r == 'A':
        r = 1
    if r == 'T':
        r = 10
    if r == 'J':
        r = 11
    if r == 'Q':
        r = 12
    if r == 'K':
        r = 13
    checkArr[int(r)-1] = checkArr[int(r)-1] + 1

bigSum = 0
for c in checkArr:
    if c > bigSum:
        bigSum = c
print(bigSum)
