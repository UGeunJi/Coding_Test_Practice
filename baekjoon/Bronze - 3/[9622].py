cnt = 0

for _ in range(int(input())):
    y, x, d, w = map(float, input().split())
    if (y > 56 or x > 45 or d > 25) and y + x + d > 125 or w > 7:
        print(0)
        continue
    print(1)
    cnt += 1
  
print(cnt)
