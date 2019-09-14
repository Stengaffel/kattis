import sys

inputs = int( sys.stdin.readline() )

for i in sys.stdin:
    i = str(i).strip()
    sum = 0
    check = 0

    for ind in range(len(i)-1,-1,-1):
        check = check + 1
        dig = int( i[ind] )

        if( check % 2 != 0 ):
            sum = sum + dig
            continue

        if( (2 * dig) > 9 ):
            sum = sum + (2 * dig) % 10
            sum = sum + (2 * dig) // 10
        else:
            sum = sum + 2 * dig

    if( sum % 10 == 0 ):
        print("PASS")
    else:
        print("FAIL")
