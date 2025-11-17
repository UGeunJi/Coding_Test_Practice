n = int(input())
x = int(input())
 
c = n * (1 - x / 100)
y = (n / c - 1) * 100
 
print(f"{y:.6f}")
