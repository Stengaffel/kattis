import sys

nums = sys.stdin.readline().split()

junc = int( nums[0] )
swits = int( nums[1] )

if swits % 2 == 1:
    print('{}'.format('impossible'))
else:
    print('{}'.format('possible'))