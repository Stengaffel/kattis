import sys

# Returns a string that has been expanded by z
def expand_columns(x,z):
    new_x = ''
    for ch in x:
        for p in range(0,z):
            new_x = new_x + ch
    return new_x


base = sys.stdin.readline().split()
r = int( base[0] )
c = int( base[1] )
zr = int( base[2] )
zc = int( base[3] )

mat = []

for i in sys.stdin:
    mat.append( str( i ).strip() )
    if len(mat) == r:
        break

# Expand columns
if zc > 1:
    for ind in range(0,len(mat)):
        mat[ind] = expand_columns(mat[ind],zc)

for t in range(0, len(mat)):
    for u in range(0, zr):
        print(mat[t])