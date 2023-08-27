b = 1000000000
r = b

for i in range(int(input())):
    x, y = map(int, input().split())
    
    if x <= y:
        r = min(r, y)
        
if b == r:
    print(-1)
else:
    print(r)
