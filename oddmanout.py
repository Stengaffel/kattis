import sys

test_cases = int( sys.stdin.readline() )

runs = 0
for i in sys.stdin:
    guests = [int(x) for x in sys.stdin.readline().split()]

    found = False
    guest_num = 0

    check = set([])
    for g in range(0,len(guests)):
        if guests[g] not in check:
            if g == len(guests)-1:
                guest_num = guests[g]
                found == True
                break
            for j in range(g+1,len(guests)):
                if guests[g] == guests[j]:
                    check.add(guests[g])
                    break
                if j == len(guests)-1:
                    found = True
                    guest_num = guests[g]
        if found:
            break
    runs = runs + 1
    print('Case #{}: {}'.format(runs,guest_num))

    if runs == test_cases:
        break
