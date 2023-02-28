import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

su = [0]
temp = 0    
for i in arr:
    temp += i
    su.append(temp)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(su[b] - su[a - 1])
