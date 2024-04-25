l, r, a=map(int,input().split())
print(min(l + a, r + a, l + r + a >> 1) * 2)
