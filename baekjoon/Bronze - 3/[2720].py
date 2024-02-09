changes = [25, 10, 5, 1]
T = int(input())

for _ in range(T) :
    C = int(input())
    res = []

    for i in changes :
        res.append(C // i)
        C = C % i
        
    print(*res)
