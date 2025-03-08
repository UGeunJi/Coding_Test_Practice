import sys

N = int(sys.stdin.readline())
v = [int(sys.stdin.readline()) for _ in range(N)]

carlos = v[0]
max_vote = max(v)

if max_vote <= carlos:
    print('S')
else:
    print('N')
