import sys

cards = str( sys.stdin.readline() ).strip()

nums = [0, 0, 0]

for ch in cards:
    if ch == 'T':
        nums[0] = nums[0] + 1
    if ch == 'C':
        nums[1] = nums[1] + 1
    if ch == 'G':
        nums[2] = nums[2] + 1

smallest = nums[0]
for n in nums:
    if n < smallest:
        smallest = n

points = nums[0]**2 + nums[1]**2 + nums[2]**2 + smallest*7

print('{}'.format(points))
