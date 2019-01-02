import sys

for i in sys.stdin:
    i = i.split()
    num = int( i[0] )
    den = int( i[1] )

    if num == 0 and den == 0:
        break

    new_num = 0
    wholes = 0
    if num < den:
        new_num = num
    else:
        wholes = num // den
        new_num = num - wholes * den

    print('{} {} / {}'.format(wholes,new_num,den))