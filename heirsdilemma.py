import sys

# Checks if the digit dig apppears in the number x
def check_digit(x, dig):
    while x > 0:
        if x % 10 == dig:
            return True
        x = x // 10
    return False

def find_nums(upper, lower, cur_num, nums, dec):
    if dec == 0:
        nums.append(cur_num)
        return
    for i in range(1,10):
        if check_digit(cur_num,i) == False and \
                        cur_num + i*dec >= ( lower // dec ) * dec:
            if cur_num + i*dec <= ( upper // dec ) * dec:
                find_nums(upper,lower,cur_num+i*dec,nums,dec//10)
            else:
                break
    return nums

bounds = [int(x) for x in sys.stdin.readline().split()]

upper = bounds[1]
lower = bounds[0]

nums = find_nums(upper,lower,0,[],10**5)

count = 0
for n in nums:
    temp_num = n

    while temp_num > 0:
        if n % ( temp_num % 10 ) != 0:
            break
        temp_num = temp_num // 10
    
    if temp_num == 0:
        count = count + 1

print('{}'.format(count))