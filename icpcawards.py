import sys

limit = int( sys.stdin.readline() )

unis = set([])
winners = []


runs = 0
for i in sys.stdin:
    cop = i.split().copy()

    cop = [ str(x).strip() for x in cop ]
    i = str(i).strip()

    if len(winners) < 12 and cop[0] not in unis:
        winners.append(i)
        unis.add(cop[0])
    runs = runs + 1
    if runs == limit:
        break

for w in winners:
    print('{}'.format(w))
