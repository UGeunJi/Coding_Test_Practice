n = int(input()); m = int(input())
max_p = 0
for _ in range(n):
    a, b = map(int, input().split())
    m = m+a-b
    if m < 0:
        max_p = 0
        break
    if max_p < m:
        max_p = m
print(max_p)
