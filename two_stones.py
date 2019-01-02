import sys

for i in sys.stdin:
    if( int(i) % 2 == 0 ):
        print('Bob')
    else:
        print('Alice')
