n = int(input())

if n == 0: 
  print(1)
elif n == 1: 
  print(0)
elif n % 2 == 0: 
  print("8" * (n // 2))
else: 
  print("4" + "8" * (n // 2))
