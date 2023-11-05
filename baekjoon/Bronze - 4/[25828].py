a, b, c = map(int, input().split())
ans = 0

if a * b < a + c * b: 
    ans = 1
elif a * b > a + c * b: 
    ans = 2
    
print(ans)
