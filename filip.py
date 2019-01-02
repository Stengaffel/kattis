import sys

# Returns the flipped representation of x e.g. 123 -> 321
def flipNum(x):
    tempArr = []
    while ( x != 0 ):
        tempArr.append(x % 10)
        x = x // 10
    newNum = 0
    dec = 1
    for i in range(len(tempArr)-1,-1,-1):
        newNum = newNum + dec * tempArr[i]
        dec = dec * 10
    return newNum

a = sys.stdin.readline()
a = a.split()

n1 = int(a[0])
n2 = int(a[1])

n1 = flipNum(n1)
n2 = flipNum(n2)

if ( n1 > n2 ):
    print(n1)
else:
    print(n2)
