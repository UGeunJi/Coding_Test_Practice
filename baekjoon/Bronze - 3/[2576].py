res = []

for _ in range(7) :
    n = int(input())
    if n % 2 != 0 :
        res.append(n)
        
if res == [] :
    print(-1)
else :
    print(sum(res))
    print(min(res))
