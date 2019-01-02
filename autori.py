import sys

a = sys.stdin.readline()
b = str(a)
c = b.split('-')

accs = []

for i in c:
    accs.append(i[0])

short = ''
for k in accs:
    short = short + k

print(short)
