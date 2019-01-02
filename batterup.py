import sys

at_bats = int( sys.stdin.readline() )

at_bat_sum = 0
denom = 0

bats = sys.stdin.readline().split()

for i in bats:
    if int(i) > -1:
        at_bat_sum = at_bat_sum + int(i)
        denom = denom + 1

print( at_bat_sum / denom)