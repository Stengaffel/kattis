import sys

tcases = int( sys.stdin.readline() )
curCase = 0

while curCase < tcases:
    curLimit = int( sys.stdin.readline() )
    visits = []
    for i in sys.stdin:
        visits.append(str(i))
        if len(visits) == curLimit:
            break
    cities = []
    for k in visits:
        if k not in cities:
            cities.append(k)
    print(len(cities))


    curCase = curCase + 1
