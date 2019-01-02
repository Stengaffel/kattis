import sys

size = int( sys.stdin.readline() )
temps = sys.stdin.readline().split()
belowz = 0
for i in temps:
    if int(i) < 0:
        belowz = belowz + 1

print(belowz)