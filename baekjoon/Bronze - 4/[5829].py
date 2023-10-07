D, H, M = map(int, input().split())
t1 = D*24*60 + H*60 + M
t2 = 11*24*60 + 11*60 + 11
t = t1 - t2
if t < 0:
    print(-1)
else:
    print(t)
