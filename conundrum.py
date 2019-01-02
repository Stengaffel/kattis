import sys

word = str( sys.stdin.readline() ).strip()
per = 'PER'
swaps = 0

for i in range(0, len(word)):
    if word[i] != per[i%3]:
        swaps = swaps + 1
print(swaps) 