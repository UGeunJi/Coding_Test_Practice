import sys

n, m=map(int,sys.stdin.readline().split())
cnt=[0] * (n + 1)

for i in range(m):
    a, b=map(int, sys.stdin.readline().split())
    cnt[a] += 1
    cnt[b] += 1

for i in range(1, n + 1):
    print(cnt[i])
