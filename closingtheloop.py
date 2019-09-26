import sys

cases = int( sys.stdin.readline() )

for x in range(0,cases):
    amount = int( sys.stdin.readline() )
    ropes = [ str(x) for x in sys.stdin.readline().strip().split() ]

    red = []
    blue = []

    for i in ropes:
        length = int( i[0:(len(i)-1)] )

        if ( ord(i[len(i)-1]) == 82 ):
            red.append(length)
        else:
            blue.append(length)
    
    red.sort(reverse=True)
    blue.sort(reverse=True)

    loop_length = 0
    used_ropes = 0

    for j in range(0, min(len(red),len(blue))):
        loop_length = loop_length + red[j] + blue[j]
        used_ropes = used_ropes + 2

    if ( loop_length > 0 ):
        loop_length = loop_length - used_ropes

    print("Case #{}: {}".format(x+1,loop_length))
