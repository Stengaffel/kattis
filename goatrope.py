import sys
import math

pos = [ int(x) for x in sys.stdin.readline().split() ]

x = pos[0]
y = pos[1]

x1 = pos[2]
y1 = pos[3]

x2 = pos[4]
y2 = pos[5]

min_dist = 0

# If inside rectangle height
if y >= y1 and y <= y2:
    if math.fabs(x - x1) < math.fabs(x - x2):
        min_dist = math.fabs(x - x1)
    else:
        min_dist = math.fabs(x - x2)
else:
    # If inside rectangle width
    if x >= x1 and x <= x2:
        if math.fabs(y - y1) < math.fabs(y - y2):
            min_dist = math.fabs(y - y1)
        else:
            min_dist = math.fabs(y - y2)
    # x,y outside corners
    else:
        # Upper right
        if x > x2 and y > y2:
            min_dist = math.sqrt( (x-x2)**2 + (y-y2)**2 )
        # Upper left
        if x < x1 and y > y2:
            min_dist = math.sqrt( (x-x1)**2 + (y-y2)**2 )
        # Lower left
        if x < x1 and y < y1:
            min_dist = math.sqrt( (x-x1)**2 + (y-y1)**2 )
        # Lower right
        if x > x2 and y < y1:
            min_dist = math.sqrt( (x-x2)**2 + (y-y1)**2 )

print('{}'.format(min_dist))