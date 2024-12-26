t = int(input())

for _ in range(t):
    n = int(input())
    res = 0
    
    for i in range(n):
        if i % 2 == 1:
            res += i

    print(res + n)
