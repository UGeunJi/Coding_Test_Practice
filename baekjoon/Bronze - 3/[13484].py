x = int(input())
n = int(input())

res = x * (n + 1)
for _ in range(n):
    p = int(input())
    res -= p
  
print(res)
