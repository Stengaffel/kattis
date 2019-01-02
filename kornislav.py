import sys

def bubble_sort(x):
    tempArr = x.copy()
    for i in range(0,len(tempArr)):
        for j in range(0,len(tempArr)-1-i):
            if tempArr[j] > tempArr[j+1]:
                temp = tempArr[j]
                tempArr[j] = tempArr[j+1]
                tempArr[j+1] = temp
    return tempArr

steps = [ int(x) for x in sys.stdin.readline().split() ]
steps_sorted = bubble_sort(steps)

print('{}'.format(steps_sorted[0] * steps_sorted[2]))