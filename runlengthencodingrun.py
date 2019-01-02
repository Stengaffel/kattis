import sys

def encode(x):
    new_str = ''
    ind = 0
    while ind < len(x):
        if ind != len(x)-1 and x[ind] == x[ind+1]:
            cur_ind = ind + 2
            while cur_ind < len(x) and x[cur_ind] == x[ind]:
                cur_ind = cur_ind + 1
            new_str = new_str + '{}{}'.format(x[ind],cur_ind-ind)
            ind = cur_ind
        else:
            new_str = new_str + '{}{}'.format(x[ind],1)
            ind = ind + 1
    return new_str


def decode(x):
    new_str = ''
    for i in range(0,len(x)):
        if ord(x[i]) < 58 and ord(x[i]) > 48:
            for j in range(1,int(x[i])):
                new_str = new_str + x[i-1]
        else:
            new_str = new_str + x[i]
    return new_str

input = sys.stdin.readline().split()

mode = str( input[0] ).strip()
line = str( input[1] ).strip()

if mode == 'E':
    print('{}'.format(encode(line)))
else:
    print('{}'.format(decode(line)))