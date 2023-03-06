import sys

n, m = map(int, sys.stdin.readline().split())

d = {}

for i in range(1, n + 1):
    a = sys.stdin.readline().rstrip()
    d[i] = a
    d[a] = i

for i in range(m):
    s = sys.stdin.readline().rstrip()
    if s.isdigit():
        print(d[int(s)])
    else:
        print(d[s])
