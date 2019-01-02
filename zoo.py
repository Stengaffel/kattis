import sys

lists = []

for length in sys.stdin:
    length = int( length )

    if length == 0:
        break

    cur_dict = {}

    runs = 0
    for i in sys.stdin:
        i = [str(x).strip() for x in i.split()]
        animal = ''
        if len(i) == 1:
            animal = i[0].lower()
        else:
            animal = i[len(i)-1].lower()
        
        if animal in cur_dict:
            cur_dict[animal] = cur_dict[animal] + 1
        else:
            cur_dict[animal] = 1
        runs = runs + 1
        if runs == length:
            break

    lists.append(cur_dict)

for i in range(0,len(lists)):
    print('List {}:'.format(i+1))
    for key in sorted(lists[i].keys()):
        print('{} | {}'.format(key,lists[i][key]))