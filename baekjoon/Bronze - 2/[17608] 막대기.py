import sys

input = sys.stdin.readline

n = int(input())
arr = []
answer = 1

for _ in range(n):
    arr.append(int(input()))

base = arr[-1]    
               
for i in range(len(arr)-2, -1, -1):
    if arr[i] > base:
        base = arr[i]
        answer += 1
               
print(answer)
