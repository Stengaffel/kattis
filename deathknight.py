import sys

test_cases = int( sys.stdin.readline() )

wins = test_cases

runs = 0
for i in sys.stdin:
    i = str(i)
    for ind in range(0,len(i)):
        if i[ind] == 'C':
            if i[ind+1] == 'D':
                wins = wins - 1
    runs = runs + 1
    if runs == test_cases:
        break
print('{}'.format(wins))