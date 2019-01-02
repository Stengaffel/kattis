import sys

x = []
y = []

for i in sys.stdin:
    i = i.split()
    x.append(int(i[0]))
    y.append(int(i[1]))
    if len(x) == 3:
        break

x_types = []
y_types = []

x_sum = 0
y_sum = 0

for k in range(0,3):
    x_sum = x_sum + x[k]
    y_sum = y_sum + y[k]

    if x[k] not in x_types:
        x_types.append(x[k])
    if y[k] not in y_types:
        y_types.append(y[k])

print( "{} {}".format( ( 2 * ( x_types[0] + x_types[1] ) ) - x_sum,( ( 2 * ( y_types[0] + y_types[1] ) ) - y_sum ) ))