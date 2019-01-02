import sys

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

limit = int(sys.stdin.readline())

nums = []

for i in sys.stdin:
    nums.append(int(i))
    if len(nums) == limit:
        break

for n in nums:
    print( factorial(n) % 10)
