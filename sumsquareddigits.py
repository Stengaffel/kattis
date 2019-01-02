import sys

inputs = int( sys.stdin.readline() )

k =[]
b = []
n = []
runs = 1

for i in sys.stdin:
    i = i.split()
    k = int( i[0] )
    b = int( i[1] )
    n = int( i[2] )
    tempb = 1
    while ( n // tempb ) >= b:
        tempb = tempb * b
    curNum = n
    a = []
    while curNum != 0:
        a.append(curNum // tempb)
        curNum = curNum % tempb
        tempb = tempb // b
    tempSum = 0
    for c in a:
        tempSum = tempSum + c ** 2
    print('{} {}'.format(k, tempSum))
    if runs == inputs:
        break
    runs = runs + 1