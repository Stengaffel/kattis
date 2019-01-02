import sys

mar = str( sys.stdin.readline() ).strip()
doc = str( sys.stdin.readline() ).strip()

if len(mar) >= len(doc):
    print('{}'.format('go'))
else:
    print('{}'.format('no'))