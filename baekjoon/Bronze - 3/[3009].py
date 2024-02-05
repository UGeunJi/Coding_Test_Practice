t1, t2 = [], []

for i in range(3):
    a, b = map(int, input().split())
    t1.append(a)
    t2.append(b)
    
for i in range(3):
    if t1.count(t1[i]) == 1:
        ans1 = t1[i]
    if t2.count(t2[i]) == 1:
        ans2 = t2[i]
        
print(f'{ans1} {ans2}')
