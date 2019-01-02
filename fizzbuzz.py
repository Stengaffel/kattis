import sys

nums = sys.stdin.readline().split()

for i in range(1, int(nums[2])+1):
    if i % int(nums[0]) == 0 and i % int(nums[1]) == 0:
        print('FizzBuzz')
        continue
    if i % int(nums[0]) == 0:
        print('Fizz')
        continue
    if i % int(nums[1]) == 0:
        print('Buzz')
        continue
    print(i) 