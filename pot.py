import sys

limit = int(sys.stdin.readline())
nums = []

for i in sys.stdin:
    nums.append(int(i))
    if len(nums) == limit:
        break

X = 0
for p in nums:
    exp = p % 10
    p = p // 10
    X = X + p**exp
print(X)
