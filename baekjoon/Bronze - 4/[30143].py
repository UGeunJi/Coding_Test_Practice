t = int(input())

for i in range(t):
    n, a, d = map(int, input().split())
    last = a + (n - 1) * d
    
    print(n * (a + last) // 2)
