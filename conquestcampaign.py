import sys

base = [int(x) for x in sys.stdin.readline().split()]

mat = []
for i in range(0,base[0]):
    mat.append([])
    for j in range(0,base[1]):
        mat[i].append(0)

start = []
for i in sys.stdin:
    i = [int(x) for x in i.split()]
    start.append(i)
    if len(start) == base[2]:
        break

for s in start:
    mat[s[0]-1][s[1]-1] = 1

days = 1
while True:
    conq = True
    for i in range(0,base[0]):
        for j in range(0,base[1]):
            if mat[i][j] == 0:
                conq = False
    if conq:
        break

    for i in range(0,base[0]):
        for j in range(0,base[1]):
            if mat[i][j] == days:
                if j < len(mat[i])-1 and mat[i][j+1] < 1:
                    mat[i][j+1] = days + 1
                if i < len(mat)-1 and mat[i+1][j] < 1:
                    mat[i+1][j] = days + 1
                if j > 0 and mat[i][j-1] < 1:
                    mat[i][j-1] = days + 1
                if i > 0 and mat[i-1][j] < 1:
                    mat[i-1][j] = days + 1
    days = days + 1
print('{}'.format(days))