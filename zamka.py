import sys

# Returns the sum of all the digits in the number 'x'
def numSum(x):
    digits = []
    while( x != 0 ):
        digits.append(x % 10)
        x = x // 10
    sum = 0
    for d in digits:
        sum = sum + d
    return sum

nums = []
for i in sys.stdin:
    nums.append(int(i))

    if( len(nums) == 3 ):
        NM = []
        for j in range(nums[0],nums[1]+1):
            if( numSum(j) == nums[2] ):
                NM.append(j)
                break
        for k in range(nums[1],nums[0]-1,-1):
            if( numSum(k) == nums[2] ):
                NM.append(k)
                break
        print("{}\n{}".format(NM[0],NM[1]))
