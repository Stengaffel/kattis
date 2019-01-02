import sys

dims = [int(x) for x in sys.stdin.readline().split()]
mat = []

smash = {
    '0': 0,
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0
}

for i in sys.stdin:
    temp_arr = []
    for ch in str(i).strip():
        temp_arr.append(ch)
    mat.append(temp_arr)
    if len(mat) == dims[0]:
        break
for i in range(0,dims[0]-1):
    for j in range(0,dims[1]-1):
        if any(x == '#' for x in \
                [mat[i][j],mat[i][j+1],mat[i+1][j],mat[i+1][j+1]]):
            continue
        else:
            cur_smash = 0
            for temp_i in range(i,i+2):
                for temp_j in range(j,j+2):
                    if mat[temp_i][temp_j] == 'X':
                        cur_smash = cur_smash + 1
            smash[str(cur_smash)] = smash[str(cur_smash)] + 1
for key,value in smash.items():
    print('{}'.format(value))

