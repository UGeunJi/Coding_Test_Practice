n = int(input())
max_T, min_B = 1, 5000
 
for _ in range(n):
    t, b = map(int, input().split())
    max_T = max(max_T, t)
    min_B = min(min_B, b)

print((max_T * min_B) % 7 + 1)
