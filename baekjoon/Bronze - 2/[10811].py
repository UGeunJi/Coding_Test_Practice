n, m = map(int, input().split())
basket = []
for i in range(n):
    basket.append(i + 1)
        
for j in range(m):
    a, b = map(int, input().split())
    basket[a - 1 : b] = basket[a - 1 : b][::-1]

print(*basket)
