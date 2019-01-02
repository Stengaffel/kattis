import sys

name = str( sys.stdin.readline() ).strip()

new_name = ''
cur_char = ''
for ch in name:
    if cur_char == ch:
        continue
    else:
        new_name = new_name + ch
        cur_char = ch

print(new_name)