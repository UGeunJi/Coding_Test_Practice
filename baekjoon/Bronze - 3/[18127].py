a, b = map(int,input().split())
aa = 1
bb = 1

for i in range(b):
    aa += a - 2
    bb += aa

print(bb)
