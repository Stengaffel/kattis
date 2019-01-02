import sys

limit = int( sys.stdin.readline() )

runs = 0
for i in sys.stdin:
    i = i.split()

    K = int( i[0] )
    N = int( i[1] )

    pos_sum = int( ( N / 2 ) * ( 1 + N ) )
    odd_sum = int( ( N / 2 ) * ( 1 + 2*(N-1) + 1) )
    even_sum = int( ( N / 2 ) * ( 2 + 2*N ) )

    print('{} {} {} {}'.format(K, pos_sum, odd_sum, even_sum))
        
    runs = runs + 1
    if runs == limit:
        break