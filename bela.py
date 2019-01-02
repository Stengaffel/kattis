import sys

conv = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7
}

dom = (0, 0, 14, 10, 20, 3, 4, 11)
ndom = (0, 0, 0, 10, 2, 3, 4, 11)

base = sys.stdin.readline().split()
hands = int( base[0] )
B = str( base[1] )

cards = []

for i in sys.stdin:
    cards.append( str(i) )
    if len(cards) == 4*hands:
        break

sum = 0
for c in cards:
    strong = False
    if c[1] == B:
        strong = True
    if strong:
        sum = sum + dom[ conv[ c[0] ] - 7 ]
    else:
        sum = sum + ndom[ conv[ c[0] ] - 7 ]
print(sum)
