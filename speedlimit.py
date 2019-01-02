import sys

for i in sys.stdin:
    if int( i ) == -1:
        break

    s = 0
    runs = 0
    temp_time = 0

    for j in sys.stdin:
        j = j.split()
        
        v = float( j[0] )
        t = float( j[1] ) - temp_time
        temp_time = float( j[1] )
        s = s + int( v * t )

        runs = runs + 1
        
        if runs == int(i):
            break
    
    
    print('{} miles'.format(s))

    
    