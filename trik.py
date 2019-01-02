import sys

a = sys.stdin.readline()
a = str(a.strip())

temp = 1
for i in a:
    if ( i == 'A' and temp != 3 ):
        if ( temp == 2 ):
            temp = 1
        else:
            temp = 2

    if ( i == 'B' and temp != 1 ):
        if ( temp == 3 ):
            temp = 2
        else:
            temp = 3

    if ( i == 'C' and temp != 2 ):
        if ( temp == 3 ):
            temp = 1
        else:
            temp = 3
print(temp)
