import sys

def digit_sum(x):
    sum = 0
    while x != 0:
        sum = sum + x % 10
        x = x // 10
    return sum

for i in sys.stdin:
    test_num = int( i )

    if test_num == 0:
        break

    count = 11
    while digit_sum(test_num) != digit_sum(count * test_num):
        count = count + 1
    print('{}'.format(count))