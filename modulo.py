import sys

check = set([])
uniques = 0

for i in range(0, 10):
    num = int( sys.stdin.readline() )
    mod = num % 42

    if mod in check:
        continue
    else:
        uniques = uniques + 1
        check.add(mod)
print('{}'.format(uniques))