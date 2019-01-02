import sys

test_cases = int( sys.stdin.readline() )

runs = 0
for i in sys.stdin:
    i = str(i).strip()
    if i == 'P=NP':
        print('{}'.format('skipped'))
        continue
    
    nums = [int(x) for x in i.split('+')]
    sum = nums[0] + nums[1]

    print('{}'.format(sum))

    runs = runs + 1
    if runs == test_cases:
        break