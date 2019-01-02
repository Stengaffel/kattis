import sys

pieces = (1, 1, 2, 2, 2, 8)

in_set = sys.stdin.readline().split()
comp_set = []

for i in range(0,len(pieces)):
    comp_set.append( pieces[i] - int(in_set[i]) )

print('{} {} {} {} {} {}'.format(comp_set[0],comp_set[1],
        comp_set[2],comp_set[3],comp_set[4],comp_set[5]))