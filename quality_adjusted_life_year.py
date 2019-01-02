import sys


length = 0
hap = []
time = []

for i in sys.stdin:
    ab = i.split()
    if len(ab) == 1 :
        length = int(ab[0])
    else:
        hap.append(float(ab[0]))
        time.append(float(ab[1]))

        if( len(hap) == length ):
            QALY = 0
            for ind in range(0,len(hap)):
                QALY = QALY + hap[ind] * time[ind]
            print(QALY)
