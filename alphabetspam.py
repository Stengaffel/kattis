import sys

line = str( sys.stdin.readline() ).strip()

# 33 <= char <= 126

tot_chars = len( line )

blanks = 0
low_case = 0
upper_case = 0
symbols = 0

for ch in line:
    if ch == '_':
        blanks = blanks + 1
        continue
    if ord(ch) > 96 and ord(ch) < 123:
        low_case = low_case + 1
        continue
    if ord(ch) > 64 and ord(ch) < 91:
        upper_case = upper_case + 1
    else:
        symbols = symbols + 1

q_blanks = blanks / tot_chars
q_low_case = low_case / tot_chars
q_upper_case = upper_case / tot_chars
q_symbols = symbols / tot_chars

print('{}'.format(q_blanks))
print('{}'.format(q_low_case))
print('{}'.format(q_upper_case))
print('{}'.format(q_symbols))