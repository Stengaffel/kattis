import sys

# Returns an array containing the binary representation of the integer 'x'
def create_binary(x):
    bin = []
    cur_dig = 2**29
    while  cur_dig > 0:
        if x >= cur_dig:
            bin.append(1)
            x = x - cur_dig
        else:
            if len(bin) > 0:
                bin.append(0)
        cur_dig = cur_dig // 2
    return bin            

# Returns an integer that is represented in binary in the array 'x'
def binary_to_num(x):
    bi_num = 0
    cur_dig = 2**( len(x)-1 )
    for i in range(0,len(x)):
        bi_num = bi_num + x[i] * cur_dig
        cur_dig = cur_dig // 2
    return bi_num

num = int( sys.stdin.readline() )

bi_arr = create_binary(num)
bi_arr.reverse()
print(binary_to_num(bi_arr))