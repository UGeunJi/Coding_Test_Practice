t = int(input())

for _ in range(t):
    s = int(input())
    n = int(input())
    price = s
    
    for _ in range(n):
        q, p = map(int, input().split())
        price += q * p
        
    print(price)
