import sys

ans_a = {
    '0': 'A',
    '1': 'B',
    '2': 'C'
}

ans_b = {
    '0': 'B',
    '1': 'A',
    '2': 'B',
    '3': 'C'
}

ans_g = {
    '0': 'C',
    '1': 'C',
    '2': 'A',
    '3': 'A',
    '4': 'B',
    '5': 'B'
}

quests = int( sys.stdin.readline() )

Ad = 0
Br = 0
Go = 0

line = str( sys.stdin.readline() ).strip()

for i in range(0,len(line)):
    cur_char = line[i]
    if cur_char == ans_a[str(i%3)]:
        Ad = Ad + 1
    if cur_char == ans_b[str(i%4)]:
        Br = Br + 1
    if cur_char == ans_g[str(i%6)]:
        Go = Go + 1

print('{}'.format(max(Ad,Br,Go)))
if Ad == max(Ad,Br,Go):
    print('{}'.format('Adrian'))
if Br == max(Ad,Br,Go):
    print('{}'.format('Bruno'))
if Go == max(Ad,Br,Go):
    print('{}'.format('Goran'))