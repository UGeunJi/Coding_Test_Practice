x, y = map(int, input().split())
cnt = 1

while 1:
    if y * cnt - x * cnt >= y:
        break
    cnt += 1

print(cnt)
