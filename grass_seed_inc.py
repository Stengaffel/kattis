import sys

l = 0
base = []
widths = []
lengths = []

for i in sys.stdin:
    if( len(base) < 2 ):
        base.append(float(i))
        continue
    if( len(base) == 2 ):
        if( base[1] > len(widths) ):
            ab = i.split()
            widths.append(float(ab[0]))
            lengths.append(float(ab[1]))
        if( len(widths) == base[1] ):
            break

rev = 0
for ind in range(0, len(widths)):
    area = lengths[ind] * widths[ind]
    rev = rev + area * base[0]

print(rev)
