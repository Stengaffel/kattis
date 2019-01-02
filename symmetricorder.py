import sys

output = []
set_count = 1

for i in sys.stdin:

    curLimit = int(i)
    if curLimit == 0:
        break
    curNames = []

    output.append('SET {}'.format(set_count))
    set_count = set_count + 1
    for j in sys.stdin:
        curNames.append( str(j).strip() )
        if len(curNames) == curLimit:
            break
    
    new_order_front = []
    new_order_back = []
    for k in range(0, len(curNames)):
        if k % 2 == 0:
            new_order_front.append(curNames[k])
        else:
            new_order_back.append(curNames[k])

    for nof in new_order_front:
        output.append(nof)
    for nob in reversed(new_order_back):
        output.append(nob)
    
for op in output:
    print(op)


