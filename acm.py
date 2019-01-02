import sys

errors = {}
solved = []

points = 0

for i in sys.stdin:
    i = i.split()

    if int(i[0]) == -1:
        break

    t = int( i[0] )
    prob = str( i[1] )
    result = str( i[2] )

    if result == 'right':
        solved.append(prob)
        points = points + t
    else:
        if prob in errors:
            errors[prob] = errors[prob] + 1
        else:
            errors[prob] = 1
for s in solved:
    if s in errors:
        points = points + errors[s] * 20

print('{} {}'.format(len(solved),points))