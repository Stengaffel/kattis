import sys

test_cases = int( sys.stdin.readline() )

for i in sys.stdin:
    i = [ float(x) for x in i.split() ]
    b = i[0]
    p = i[1]
    calc_bpm = 60 * ( b / p )
    low_abpm = 60 * ( ( b - 1 ) / p )
    high_abpm = 60 * ( ( b + 1 ) / p )

    print('{} {} {}'.format(low_abpm, calc_bpm, high_abpm))