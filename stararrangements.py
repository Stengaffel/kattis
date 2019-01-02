import sys

stars = int( sys.stdin.readline() )
print('{}:'.format(stars))

for i in range(2, stars):
    for j in range(i-1,i+1):
        temp = i + j
        while temp < stars:
            temp = temp + i + j
        if temp == stars or temp - j == stars:
            print('{},{}'.format(i,j))