import sys

code = str( sys.stdin.readline() )
decoded = ''

vowels = set(['a', 'e', 'i', 'o', 'u'])

ind = 0
while ind < len(code):
    decoded = decoded + code[ind]
    if code[ind] in vowels:
        ind = ind + 3
        continue

    ind = ind + 1

print('{}'.format(decoded))