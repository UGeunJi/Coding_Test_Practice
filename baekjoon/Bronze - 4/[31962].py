n, x = map(int, input().split())
b = []
for _ in range(n):
    s, t = map(int, input().split())
    b.append([s, t])

b.sort(key=lambda x: -x[0])

a = False
for k, d in b:
    if k + d > x:
        continue
    else:
        a = True
        t = k  # 걸리는 시간
        break

if a:
    print(t)
else:
    print(-1)
