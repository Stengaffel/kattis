import sys

limit = int( sys.stdin.readline() )

start = []
end = []

for i in sys.stdin:
    i = i.split()
    start.append( int(i[0]) )
    end.append( int(i[1]) )

    if len(start) == limit:
        break

days = []

for event in range(0,limit):
    for day in range(start[event], end[event]+1):
        if day not in days:
            days.append(day)

print(len(days))