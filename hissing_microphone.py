import sys

word = str( sys.stdin.readline() )

hiss = False
for i in range( 0, len(word)-1):
    if word[i] == 's' and word[i+1] == 's':
        hiss = True

if hiss:
    print('hiss')
else:
    print('no hiss')
