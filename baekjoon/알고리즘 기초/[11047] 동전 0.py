import sys

n, k = map(int, sys.stdin.readline().split())
arr = []

for i in range(n):
    arr.append(int(sys.stdin.readline()))

coin = 0

for i in range(len(arr)-1, -1, -1):
    if arr[i] <= k:
        while arr[i] <= k:
            k -= arr[i]
            coin += 1

print(coin)
