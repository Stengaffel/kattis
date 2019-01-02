import sys

date = sys.stdin.readline().split()

if ( str(date[0]) == 'DEC' and int(date[1]) == 25 ) or ( str(date[0]) == 'OCT' and int(date[1]) == 31 ):
    if str(date[0]) == 'DEC' and int(date[1]) == 25:
        print('yup')

    if str(date[0]) == 'OCT' and int(date[1]) == 31:
        print('yup')

else:
    print('nope')
