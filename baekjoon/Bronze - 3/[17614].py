n = int(input())
ans = 0

for i in range(1, n + 1):
    n = str(i)
    a = n.count('3')
    b = n.count('6')
    c = n.count('9')
    ans += a + b + c
    
print(ans)
