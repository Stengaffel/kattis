import sys

date = sys.stdin.readline().split()

day = int( date[0] )
month = int( date[1] )

# January 1st is a Thursday
months = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
weekdays = ('Thursday','Friday','Saturday','Sunday','Monday','Tuesday','Wednesday')

allDays = 0
for i in range(1,month):
    allDays = allDays + months[i-1]
allDays = allDays + day

print(weekdays[allDays%7 - 1])