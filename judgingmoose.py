import sys

nums = [int(x) for x in sys.stdin.readline().split()]

if nums[0] == nums[1]:
    if nums[0] == 0:
        print('{}'.format('Not a moose'))
    else:
        print('Even {}'.format(2*nums[0]))
else:
    print('Odd {}'.format(2*max(nums)))