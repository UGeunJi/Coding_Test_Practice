num = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  
n, b = map(str, input().split())

sum = 0
n = list(reversed(n))

for i in range(len(n) - 1, -1, -1):
    sum += num.index(n[i]) * (int(b) ** i)

print(sum)
