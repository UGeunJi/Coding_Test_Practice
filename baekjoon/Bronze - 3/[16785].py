a, b, c = map(int, input().split())
count = t = 0

while t < c:
    t += a
    count += 1
    if count % 7 == 0:
        t += b
      
print(count)
