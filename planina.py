import sys

a = sys.stdin.readline()

side = 2 ** int(a)
sidePoint = side + 1

totPoints = sidePoint ** 2

print(totPoints)
