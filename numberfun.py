import sys

test_cases = int( sys.stdin.readline() )

runs = 0
for i in sys.stdin:
    i = [int(x) for x in i.split()]
    if i[0] + i[1] == i[2] or i[0] * i[1] == i[2] or \
            i[0] / i[1] == i[2] or i[1] / i[0] == i[2] or \
                i[0] - i[1] == i[2] or i[1] - i[0] == i[2]:
        print('{}'.format('Possible'))
    else:
        print('{}'.format('Impossible'))

    runs = runs + 1
    if runs == test_cases:
        break