import sys

limit = int( sys.stdin.readline() )

checks = []
for i in sys.stdin:
    checks.append(str(i))

    if len(checks) == 2 * limit:
        break

for k in range(0, len(checks)):
    if k % 2 == 1:
        continue
    prString = ''
    for pos in range(0,len(checks[k])-1):
        if checks[k][pos] == checks[k+1][pos]:
            prString = prString + '.'
        else:
            prString = prString + '*'
    print(checks[k].strip())
    print(checks[k+1].strip())
    print(prString.strip())
    print('')