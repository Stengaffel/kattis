import sys

a = {
    '0': 'A',
    '1': 'B',
    '2': 'C',
    '3': 'D',
    '4': 'E',
    '5': 'F',
    '6': 'G',
    '7': 'H',
    '8': 'I',
    '9': 'J',
    '10': 'K',
    '11': 'L',
    '12': 'M',
    '13': 'N',
    '14': 'O',
    '15': 'P',
    '16': 'Q',
    '17': 'R',
    '18': 'S',
    '19': 'T',
    '20': 'U',
    '21': 'V',
    '22': 'W',
    '23': 'X',
    '24': 'Y',
    '25': 'Z'
}

code = str( sys.stdin.readline() ).strip()

s1 = code[:len(code)//2]
s2 = code[len(code)//2:]

r1 = 0
r2 = 0
for i in range(0,len(s1)):
    r1 = r1 + ord(s1[i]) - 65
    r2 = r2 + ord(s2[i]) - 65

chars1 = []
chars2 = []

final_chars = []
s = ''

for i in range(0,len(s1)):
    chars1.append( ( ord(s1[i]) - 65 + r1 ) % 26 )
    chars2.append( ( ord(s2[i]) - 65 + r2 ) % 26 )
    final_chars.append( (chars1[i] + chars2[i]) % 26 )
    s = s + a[str( final_chars[i] )]

print('{}'.format(s))