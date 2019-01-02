import sys

nums = []
length = 0

for i in sys.stdin:
    nums.append(int(i))

    if ( len(nums) == 2 ):
        length = nums[1] + 2
    if( len(nums) == length ):
        break

totMeg = nums[0] * ( nums[1] + 1 )
curMeg = 0

for i in range(2, len(nums)):
    curMeg = curMeg + nums[i]

print(totMeg-curMeg)
