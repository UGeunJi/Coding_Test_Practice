import sys

n, m = map(int, sys.stdin.readline().split())
site = []
key = []

for i in range(n):
    s = sys.stdin.readline().split()
    site.append(s[0])
    key.append(s[1])

answer = []

for i in range(m):
    answer.append(key[site.index(sys.stdin.readline().rstrip())])

print(*answer, sep='\n')
