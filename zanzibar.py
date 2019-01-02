import sys

test_cases = int( sys.stdin.readline() )
runs = 0
for i in sys.stdin:
    i = i.split()
    curSum = 0
    for ind in range(1,len(i)):
        if int(i[ind]) > 2*int(i[ind-1]):
            curSum = curSum + int(i[ind]) - 2*int(i[ind-1])
    print(curSum)
    runs = runs + 1
    if runs == test_cases:
        break