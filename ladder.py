import sys
import math

a = sys.stdin.readline().split()

print( int( int(a[0]) // math.sin(math.radians(int(a[1]))) + 1 ) )
