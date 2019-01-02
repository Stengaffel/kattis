import sys

cipher = str( sys.stdin.readline() ).strip()
key = str( sys.stdin.readline() ).strip()

new_str = ''

length = min(len(cipher),len(key))

for i in range(0,length):
    c_char = ord(cipher[i]) - 65
    k_char = ord(key[i]) - 65
    new_char = c_char - k_char
    if new_char < 0:
        new_char = new_char + 26
    new_str = new_str + chr(new_char + 65)

for i in range(len(key),len(cipher)):
    c_char = ord(cipher[i]) - 65
    k_char = ord(new_str[i-len(key)]) - 65
    new_char = c_char - k_char
    if new_char < 0:
        new_char = new_char + 26
    new_str = new_str + chr(new_char + 65)

print('{}'.format(new_str))