import sys

base = sys.stdin.readline().split()

N = base[0]
limit = base[1]

initial_locs = sys.stdin.readline().split()
locations = []

runs = 0
for l in initial_locs:
    locations.append(int(l))
    runs = runs + 1
    if runs == N:
        break

runs = 0
for i in sys.stdin:
    i = [int(x) for x in i.split()]
    if i[0] == 1:
        locations[i[1]-1] = i[2]
    else:
        dist = max(locations[i[1]-1],locations[i[2]-1]) - min(
                                    locations[i[1]-1],locations[i[2]-1])
        print('{}'.format(dist))

    runs = runs + 1
    if runs == limit:
        break

