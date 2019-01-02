import sys

nums = sys.stdin.readline().split()

vic_card = ''
t_card = ''

b_power = int( nums[0] ) * 3 + int( nums[1] ) * 2 +int( nums[2] ) * 1

if b_power >= 0 and b_power < 3:
    t_card = 'Copper'
if b_power >= 3 and b_power < 6:
    t_card = 'Silver'
if b_power >= 6:
    t_card = 'Gold'

if b_power >= 2 and b_power < 5:
    vic_card = 'Estate'
if b_power >= 5 and b_power < 8:
    vic_card = 'Duchy'
if b_power >= 8:
    vic_card = 'Province'

if len(vic_card) > 0 and len(t_card) > 0:
    print('{} or {}'.format(vic_card,t_card))
if len(vic_card) > 0 and len(t_card) == 0:
    print('{}'.format(vic_card))
if len(vic_card) == 0 and len(t_card) > 0:
    print('{}'.format(t_card))