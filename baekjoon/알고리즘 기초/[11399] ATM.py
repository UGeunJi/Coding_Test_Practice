import sys

n = int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.readline().split())))
su = 0
min = []
for i in range(len(arr)):
    su += arr[i]
    min.append(su)

print(sum(min))
