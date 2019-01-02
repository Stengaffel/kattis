import sys

for i in sys.stdin:
    a = i.split()
    nums = [int(a[0]), int(a[1])]
    if( len(nums) == 2):
        upperLim = nums[0] * nums[1]
        test = upperLim / nums[0]
        while( test > nums[1] - 1 ):
            upperLim = upperLim - 1
            test = upperLim / nums[0]
        print(upperLim+1)
