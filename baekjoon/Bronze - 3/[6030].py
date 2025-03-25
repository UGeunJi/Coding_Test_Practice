p, q = map(int, input().split())
l1, l2 = [], []

for i in range(1, max(p, q) + 1):
    if p % i == 0: 
        l1.append(i)
    if q % i == 0: 
        l2.append(i)

for j in l1:
    for z in l2:
        print(i, z)
