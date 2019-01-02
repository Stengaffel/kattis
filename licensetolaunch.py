import sys

days = int( sys.stdin.readline() )
junk = [ int(x) for x in sys.stdin.readline().split() ]
smallest = junk[0]
for j in junk:
    if j < smallest:
        smallest = j

l_day = 0

for i in range(0, len(junk)):
    if smallest == junk[i]:
        l_day = i
        break

print('{}'.format(l_day))

