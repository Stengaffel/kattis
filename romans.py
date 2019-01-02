import sys

e_miles = float( sys.stdin.readline() )

r_paces = e_miles * 1000 * ( 5280 / 4854 )

if r_paces % 1 >= 0.500:
    r_paces = int( r_paces ) + 1

print( '{}'.format(int( r_paces )))