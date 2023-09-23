r, c, n = map(int, input.split())

if r % n:
  x = r // n + 1
else:
  x = r // n
  
if c % n:
  y = c // n + 1
else:
  y = c // n

print(x * y)
