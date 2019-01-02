import sys
import math

dct = {}

val = 1
for i in range(65,91):
    dct[str(chr(i))] = val
    val = val + 1
dct[' '] = 27
dct['\''] = 28

one_dist = ( math.pi * 60 ) / 28
one_time = one_dist / 15

limit = int( sys.stdin.readline() )

runs = 0
for line in sys.stdin:
    line = str(line).strip()
    tot_time = 1

    cur_place = dct[line[0]]
    for i in range(1,len(line)):
        next = dct[line[i]]
        tot_time = tot_time + min(math.fabs(cur_place-next),
                    ( 28-math.fabs(cur_place-next))) * one_time + 1
        cur_place = next
    
    print('{}'.format(tot_time))

    runs = runs + 1
    if runs == limit:
        break