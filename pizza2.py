import sys
import math

base = [int(x) for x in sys.stdin.readline().split()]

r = base[0]
c = base[1]

tot_area = math.pi * r**2
cheese_area = math.pi * (r-c)**2

print('{}'.format( ( cheese_area / tot_area) * 100)) 