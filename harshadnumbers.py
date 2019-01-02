import sys

num = int( sys.stdin.readline() )

test = num
while True:
    temp = test
    num_sum = 0
    while temp != 0:
        num_sum = num_sum + ( temp % 10 )
        temp = temp // 10
    if test % num_sum == 0:
        print('{}'.format(int(test)))
        break
    test = test + 1
