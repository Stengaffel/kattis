import sys

gun = [int(x) for x in sys.stdin.readline().split()]
emma = [int(x) for x in sys.stdin.readline().split()]

g_val = ( gun[0] + gun[1] + gun[2] + gun[3] - 2 ) / 2
e_val = ( emma[0] + emma[1] + emma[2] + emma[3] - 2 ) / 2

if g_val > e_val or g_val < e_val:
    if g_val > e_val:
        print('{}'.format('Gunnar'))
    else:
        print('{}'.format('Emma'))
else:
    print('{}'.format('Tie'))