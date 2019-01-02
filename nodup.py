import sys

sent = [ str(x) for x in sys.stdin.readline().split() ]

nodup = True

for i in range(0, len(sent)):
    for j in range(i+1,len(sent)):
        if sent[i] == sent[j]:
            nodup = False
            break
    if nodup == False:
        break

if nodup:
    print('{}'.format('yes'))
else:
    print('{}'.format('no'))