import sys

limit = int(sys.stdin.readline())
nums = []

for i in sys.stdin:
    nums.append(int(i))
    if len(nums) == limit:
        break

for n in nums:
    if n % 2 == 0:
        print("{} is even".format(n))
    else:
        print("{} is odd".format(n))
