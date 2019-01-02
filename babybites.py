import sys

num = int( sys.stdin.readline() )

counting = [str(x).strip() for x in sys.stdin.readline().split()]

message = 'makes sense'
for c in range(0,len(counting)):
    if counting[c] == 'mumble':
        continue
    if int( counting[c] ) != c + 1:
        message = 'something is fishy'
        break
print('{}'.format(message))