import sys

nums = [int(x) for x in sys.stdin.readline().split()]

a = nums[0]
b = nums[1]
c = nums[2]

for i in range(0,1):
    if a + b == c:
        print('{}+{}={}'.format(a,b,c))
        break
    if a == b + c:
        print('{}={}+{}'.format(a,b,c))
        break
    if a - b == c:
        print('{}-{}={}'.format(a,b,c))
        break
    if a == b - c:
        print('{}={}-{}'.format(a,b,c))
        break
    if a * b == c:
        print('{}*{}={}'.format(a,b,c))
        break
    if a == b * c:
        print('{}={}*{}'.format(a,b,c))
        break
    if a / b == c:
        print('{}/{}={}'.format(a,b,c))
        break
    if a == b / c:
        print('{}={}/{}'.format(a,b,c))
        break