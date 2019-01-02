import sys

limit = int( sys.stdin.readline() )

runs = 0
for i in sys.stdin:
    print('{}'.format(len(str(i).strip())))

    runs = runs + 1
    if runs == limit:
        break