n = int(input())
ans = 0
p = list(map(int, input().split()))

for i in range(n):
    if p[i] != i + 1:
        ans += 1
        
print(ans)
