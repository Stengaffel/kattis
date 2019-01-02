import sys

# Worthless
def move_one(heads, tails):
    return heads, tails

def move_two(heads, tails):
    return heads, tails + 1

def move_three(heads, tails):
    return heads-2, tails

def move_four(heads, tails):
    return heads+1, tails-2

for i in sys.stdin:
    i = i.split()

    h = int( i[0] )
    t = int( i[1] )

    if h == 0 and t == 0:
        break

    moves = 0

    if h == 1 and t == 0:
        print('{}'.format(1))
        continue

    if h % 2 == 0 and t == 0:
        print('{}'.format(h // 2))
        continue

    if h % 2 == 1:
        h,t = move_four(h,t)
        moves = moves + 1
    while h > 0:
        h,t = move_three(h,t)
        moves = moves + 1
    
    while t % 4 != 0:
        h,t = move_two(h,t)
        moves = moves + 1

    while t > 0:
        h,t = move_four(h,t)
        moves = moves + 1

    while h > 0:
        h,t = move_three(h,t)
        moves = moves + 1

    print('{}'.format(moves))