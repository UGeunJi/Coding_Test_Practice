a, b, c = sorted([*map(int, input().split())])
ans = 3

if a + b == c:
    ans = 1
elif a * b == c:
    ans = 2
    
print(ans)
