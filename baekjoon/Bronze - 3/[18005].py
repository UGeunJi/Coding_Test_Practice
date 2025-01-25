n = int(input())

if n % 2:
    res = 0
elif n // 2 % 2 == 0:
    res = 2
else:
    res = 1
  
print(res)
